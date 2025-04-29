from pydantic import BaseModel
from typing import Optional

class CreateTranslation(BaseModel):
    user_id: Optional[int] = None
    input_text: Optional[str] = None
    translated_text: Optional[str] = None
    source_lang: Optional[str] = None
    target_lang: Optional[str] = None


class UpdateTranslation(BaseModel):
    user_id: Optional[int] = None
    input_text: Optional[str] = None
    translated_text: Optional[str] = None
    source_lang: Optional[str] = None
    target_lang: Optional[str] = None