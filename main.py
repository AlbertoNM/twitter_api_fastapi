# Dependencies

## Python
import json
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List

## Pydantic
from pydantic import BaseModel, Field
from pydantic import EmailStr

## FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body

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
    
class RegisterUser(User, UserLogin):
    pass

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
def signup(user: RegisterUser = Body(...)):
    """
    Signup
    ======
    ---
    This path operation register a user in the app
    
    Parameters:
    * Request body parameter:
        * user: User
    
    Returns:
    * user_id: UUID
    * email: EmailStr
    * first_name: str
    * last_name: str
    * birth_date: date
    """
    with open('users.json', 'r+', encoding = 'utf-8') as f:
        results = json.load(f)
        user_dict = user.dict()
        user_dict['user_id'] = str(user_dict['user_id'])
        user_dict['birth_date'] = str(user_dict['birth_date'])
        results.append(user_dict)
        f.seek(0)
        json.dump(results, f)
        return user

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
    """
    Showing users
    =============
    ---
    This path operation shows all users in the app

    Parameters:
    *

    Returns a json list with all users in the app, with the following keys:
    * user_id: UUID
    * email: Emailstr
    * first_name: str
    * last_name: str
    * birth_date: date
    """
    with open('users.json', 'r', encoding = 'utf-8') as f:
        results = json.load(f)
        return results

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
    response_model = List[Tweet],
    status_code = status.HTTP_200_OK
)
def home():
    """
    Home
    ====
    ---
    This path operation shows all tweets in the app

    Parameters:
    *

    Returns a json list with all tweets in the app, with the following keys:
    * tweet_id: UUID
    * content: str
    * created_at: datetime
    * update_at: datetime
    * by: User
    """
    with open('tweets.json', 'r', encoding = 'utf-8') as f:
        results = json.load(f)
        return results

### Post a tweet
@app.post(
    path = '/post',
    summary = 'Post a tweet',
    tags = ['Tweets'],
    response_model = Tweet,
    status_code = status.HTTP_201_CREATED
)
def post(tweet: Tweet = Body(...)):
    """
    Post a Tweet
    ============
    ---
    This path operation post a tweet in the app
    Parameters:
    * Request body parameter:
        * tweet: Tweet
    
    Returns:
    * tweet_id: UUID
    * content: str
    * created_at: datetime
    * update_at: datetime
    * by: User
    """
    with open('tweets.json', 'r+', encoding = 'utf-8') as f:
        results = json.load(f)
        tweet_dict = tweet.dict()
        tweet_dict['tweet_id'] = str(tweet_dict['tweet_id'])
        tweet_dict['created_at'] = str(tweet_dict['created_at'])
        if tweet_dict['update_at']:
            tweet_dict['update_at'] = str(tweet_dict['update_at'])
        tweet_dict['by']['user_id'] = str(tweet_dict['by']['user_id'])
        tweet_dict['by']['birth_date'] = str(tweet_dict['by']['birth_date'])
        results.append(tweet_dict)
        f.seek(0)
        json.dump(results, f)
        return tweet

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