from db import Base
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func

class Translation(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # Agar users jadvali bo'lsa
    input_text = Column(Text, nullable=True)
    translated_text = Column(Text, nullable=True)
    source_lang = Column(String(10), nullable=True)
    target_lang = Column(String(10), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())
