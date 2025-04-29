from pydantic import BaseModel
from typing import Optional


# --- USER SCHEMAS ---

class CreateUser(BaseModel):
    username: str
    email: str
    password: str


class UpdateUser(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None