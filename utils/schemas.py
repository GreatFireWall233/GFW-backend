from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    phone_number: str
    permission: str
    is_verified: bool


class UserCreate(UserBase):
    password: str
    area: list = []


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class AreaBase(BaseModel):
    name: str


class AreaCreate(AreaBase):
    pass


class Area(AreaBase):
    id: int
    position: str

    users: list[User] = []

    class Config:
        from_attributes = True
