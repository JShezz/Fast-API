from pydantic import BaseModel


class Base(BaseModel):
    created_at: str
    last_updated_at: str


class UserBase(BaseModel):
    email: str | None
    password: str | None
    is_active: bool | None


class UserResponse(UserBase, Base):
    id: int

    class Config:
        orm_mode = True
