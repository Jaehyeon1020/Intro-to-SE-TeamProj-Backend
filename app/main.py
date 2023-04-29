from fastapi import FastAPI, Depends
from routers import users

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# /users 라우터
app.include_router(users.router)
