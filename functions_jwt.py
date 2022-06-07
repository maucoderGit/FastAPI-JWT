from datetime import datetime, timedelta
from jwt import decode, encode
from jwt import exceptions
from os import getenv
from fastapi import status

def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date


def write_token(data: dict):
    token = encode(
        payload={**data, 'exp': expire_date(2)},
        key=getenv('SECRET'),
        algorithm='HS256'
    )

    return token

def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv('SECRET'), algorithms=['HS256'])
        decode(token, key=getenv('SECRET'), algorithms=['HS256'])
    except exceptions.DecodeError:
        return {
            'message': 'Invalid Token',
            'status_code': status.HTTP_401_UNAUTHORIZED
        }
    except exceptions.ExpiredSignatureError:
        return {
            'message': 'Token expired',
            'status_code': status.HTTP_401_UNAUTHORIZED
        }