from pydantic import BaseModel, Field


class UserBase(BaseModel):
    user_id: int
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    username: str = Field(default=None)
    is_admin: bool = Field(default=False)


class CreateUser(UserBase):
    pass


class UserOut(UserBase):
    pass
