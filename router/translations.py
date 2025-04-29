from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from madel.translations import Translation
from schemas.translations import CreateTranslation, UpdateTranslation

router = APIRouter()

@router.post("/translations/")
def create_translation(translation: CreateTranslation, db: Session = Depends(get_db)):
    db_translation = Translation(**translation.dict())
    db.add(db_translation)
    db.commit()
    db.refresh(db_translation)
    return db_translation


@router.get("/translations/{translation_id}")
def get_translation(translation_id: int, db: Session = Depends(get_db)):
    translation = db.query(Translation).filter(Translation.id == translation_id).first()
    if not translation:
        raise HTTPException(status_code=404, detail="Translation not found")
    return translation


@router.put("/translations/{translation_id}")
def update_translation(translation_id: int, translation: UpdateTranslation, db: Session = Depends(get_db)):
    db_translation = db.query(Translation).filter(Translation.id == translation_id).first()
    if not db_translation:
        raise HTTPException(status_code=404, detail="Translation not found")
    update_data = translation.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_translation, key, value)
    db.commit()
    db.refresh(db_translation)
    return db_translation


@router.delete("/translations/{translation_id}")
def delete_translation(translation_id: int, db: Session = Depends(get_db)):
    db_translation = db.query(Translation).filter(Translation.id == translation_id).first()
    if not db_translation:
        raise HTTPException(status_code=404, detail="Translation not found")
    db.delete(db_translation)
    db.commit()
    return {"detail": "Translation deleted successfully"}
