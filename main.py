# Dependencies

# Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List

# Pydantic
from pydantic import BaseModel, Field
from pydantic import EmailStr

# FastAPI
from fastapi import FastAPI
from fastapi import status

app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length = 8,
        max_length = 50
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length = 1,
        max_length = 50
        )
    last_name: str = Field(
        ...,
        min_length = 1,
        max_length = 50
        )
    birth_date: Optional[date] = Field(default = None)

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length = 1,
        max_length = 256
    )
    created_at: datetime = Field(default = datetime.now())
    update_at: Optional[datetime] = Field(default = None)
    by: User = Field(...)

# Path Operations

## Auth

### Resgister a user
@app.post(
    path = '/auth/signup',
    summary = 'Register a User',
    tags = ['Auth', 'Users'],
    response_model = User,
    status_code = status.HTTP_201_CREATED
)
def signup():
    pass

### Login a user
@app.post(
    path = '/auth/login',
    summary = 'Login a User',
    tags = ['Auth', 'Users'],
    response_model = User,
    status_code = status.HTTP_200_OK
)
def login():
    pass

## Users

### Show all users
@app.get(
    path = '/users/',
    summary = 'Show all users',
    tags = ['Users'],
    response_model = List[User],
    status_code = status.HTTP_200_OK
)
def show__all_users():
    pass

### Show a user
@app.get(
    path = '/users/{user_id}',
    summary = 'Show a user',
    tags = ['Users'],
    response_model = User,
    status_code = status.HTTP_200_OK
)
def show_a_user():
    pass

### Delete a user
@app.delete(
    path = '/users/{user_id}',
    summary = 'Delete a User',
    tags = ['Users'],
    response_model = User,
    status_code = status.HTTP_200_OK
)
def delete_a_user():
    pass

### Update a user
@app.put(
    path = '/users/{user_id}',
    summary = 'Update a User',
    tags = ['Users'],
    response_model = User,
    status_code = status.HTTP_200_OK
)
def update_a_user():
    pass

## Tweets

### Show all tweets
@app.get(
    path = '/',
    summary = 'Show all tweets',
    tags = ['Tweets'],
    # response_model = List[Tweet],
    status_code = status.HTTP_200_OK
)
def home():
    return {'Twitter api': 'Working'}

### Post a tweet
@app.post(
    path = '/post',
    summary = 'Post a tweet',
    tags = ['Tweets'],
    response_model = Tweet,
    status_code = status.HTTP_200_OK
)
def post():
    pass

### Show a tweet
@app.get(
    path = '/tweets/{tweet_id}',
    summary = 'Show a tweet',
    tags = ['Tweets'],
    response_model = Tweet,
    status_code = status.HTTP_200_OK
)
def show_a_tweet():
    pass

### Delete a tweet
@app.delete(
    path = '/tweets/{tweet_id}',
    summary = 'Delete a tweet',
    tags = ['Tweets'],
    response_model = Tweet,
    status_code = status.HTTP_200_OK
)
def delete_a_tweet():
    pass

### Update a tweet
@app.put(
    path = '/tweets/{tweet_id}',
    summary = 'Update a tweet',
    tags = ['Tweets'],
    response_model = Tweet,
    status_code = status.HTTP_200_OK
)
def update_a_tweet():
    pass