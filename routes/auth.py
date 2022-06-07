from fastapi import APIRouter, Body, Header, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field
from functions_jwt import validate_token, write_token

auth_routes = APIRouter()

class User(BaseModel):
    username: str = Field(
        ...,
        title='username',
        description='A API username'
    )
    email: EmailStr = Field(...)

@auth_routes.post(
    #description='Path to login a user in the API',
    path='/login',
    status_code=status.HTTP_200_OK,
    tags=['Home'],
    summary='Log in a user'
)
def login(user: User = Body(...)):
    """
    Login

    Path operation to login a user

    parameters:
    - Request Body parameters:
        - user: User

    Returns a JSON with a model:
    - username: str
    - email: EmailStr
    """
    if user.username == 'maucoder':
        return write_token(user.dict())
    else:
        return JSONResponse(content={'message':'user not found'}, status_code=404)
    # return {'response':'success'}


@auth_routes.post('/verify/token')
def verify_token(Authorization: str = Header(default=None)):
    token = Authorization.split(" ")[1]
    print(token)
    return validate_token(token, output=True)