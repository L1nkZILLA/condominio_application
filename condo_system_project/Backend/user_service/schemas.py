from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    full_name: str
    email: str
    hashed_password: str
    role: str
    company_id: Optional[int]

class UserOut(BaseModel):
    id: int
    full_name: str
    email: str
    role: str
    company_id: Optional[int]

    class Config:
        orm_mode = True
