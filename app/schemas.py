from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint


class UserBase(BaseModel):
    email: EmailStr
    
    
class UserCreate(UserBase):
    password: str
    

class UserResponse(UserBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode=True
        
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    owner: UserResponse

class Post(PostBase):
    pass

class PostCreate(BaseModel):
    title: str
    content: str
    published: bool = True


class PostResponse(PostBase):
    id: int
    created_at: datetime
    user_id: int
    class Config:
        orm_mode=True
    

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str]
    
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)