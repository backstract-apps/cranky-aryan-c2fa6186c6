from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple,Union

import re

class Comments(BaseModel):
    idea_id: int
    user_id: int
    content: str
    created_at_dt: Optional[Any]=None


class ReadComments(BaseModel):
    idea_id: int
    user_id: int
    content: str
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Ideas(BaseModel):
    user_id: int
    title: str
    description: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadIdeas(BaseModel):
    user_id: int
    title: str
    description: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Users(BaseModel):
    email: str
    password: str
    created_at_dt: Optional[Any]=None


class ReadUsers(BaseModel):
    email: str
    password: str
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True




class PostComments(BaseModel):
    idea_id: Union[int, float] = Field(...)
    user_id: Union[int, float] = Field(...)
    content: str = Field(..., max_length=100)
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    email: str = Field(..., max_length=255)
    password: str = Field(..., max_length=255)
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutCommentsId(BaseModel):
    id: str = Field(..., max_length=100)
    idea_id: Union[int, float] = Field(...)
    user_id: Union[int, float] = Field(...)
    content: str = Field(..., max_length=100)
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: str = Field(..., max_length=100)
    email: str = Field(..., max_length=255)
    password: str = Field(..., max_length=255)
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostIdeas(BaseModel):
    user_id: Union[int, float] = Field(...)
    title: str = Field(..., max_length=255)
    description: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutIdeasId(BaseModel):
    id: str = Field(..., max_length=100)
    user_id: Union[int, float] = Field(...)
    title: str = Field(..., max_length=255)
    description: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostPlatformAuthPackageMaysonAuthUserLogin(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostPlatformAuthPackageMaysonAuthUserRegister(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



# Query Parameter Validation Schemas

class GetCommentsIdQueryParams(BaseModel):
    """Query parameter validation for get_comments_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetUsersIdQueryParams(BaseModel):
    """Query parameter validation for get_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteCommentsIdQueryParams(BaseModel):
    """Query parameter validation for delete_comments_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetIdeasIdQueryParams(BaseModel):
    """Query parameter validation for get_ideas_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteUsersIdQueryParams(BaseModel):
    """Query parameter validation for delete_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteIdeasIdQueryParams(BaseModel):
    """Query parameter validation for delete_ideas_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True
