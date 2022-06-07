from typing import Optional
from requests import get
from fastapi import APIRouter, status
from pydantic import BaseModel, Field
from middlewares.verify_token import VerifyTokenRoute

users_github = APIRouter(route_class=VerifyTokenRoute)

class UserGithub(BaseModel):
    country: str = Field(...)
    page: Optional[int] = Field(default= None)

@users_github.post(
    path='/users/github',
    status_code=status.HTTP_202_ACCEPTED,
    tags=['Auth'],
    summary='Github User Request'
)
def github_users(github: UserGithub):
    '''
    Github Users

    Path operation to do a users request by country

    Parameters:
    - github: UserGithub

    Returns a Json with user github models by country and page.
    '''
    return get(f'https://api.github.com/search/users?q=location:{github.country}&page:{github.page}').json()
