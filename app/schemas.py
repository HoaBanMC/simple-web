from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr, constr
from bson.objectid import ObjectId

class UserBaseSchema(BaseModel):
    name: str
    email: str
    photo: str
    role: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True

class CreateUSerSchema(UserBaseSchema):
    password: constr(min_length=8, strip_whitespace=True)
    passwordConfirm: str
    verified: bool = True


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8, strip_whitespace=True)

class UserResponseSchema(UserBaseSchema):
    id: str
    pass

class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema

class FilteredUserResponse(UserBaseSchema):
    id: str

class PostBaseSchema(BaseModel):
    title: str
    content: str
    category: str
    image: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class CreatePostScheme(PostBaseSchema):
    user: ObjectId | None = None
    pass

class PostResponse(PostBaseSchema):
    id: str
    user: FilteredUserResponse
    created_at: datetime
    updated_at: datetime
