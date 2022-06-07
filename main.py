from fastapi import FastAPI
from dotenv import load_dotenv
from routes.auth import auth_routes

app = FastAPI()


@app.get(
    path='/',
    status_code=200
)
def home():
    return {'hello': 'world'}

app.include_router(auth_routes, prefix='/api')
load_dotenv()