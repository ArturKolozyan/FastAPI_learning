from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    age: int
    email: EmailStr
