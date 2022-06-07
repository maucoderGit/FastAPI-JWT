from requests import get
from fastapi import APIRouter
from pydantic import BaseModel

users_github = APIRouter()

class UserGithub(BaseModel):
    country: str
    page: str

@users_github.post('/users/github')
def github_users(github: UserGithub):
    return get(f'https://api.github.com/search/users?q=location:{github.country}&page:{github.page}').json()
