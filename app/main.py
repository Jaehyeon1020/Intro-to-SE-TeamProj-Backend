from fastapi import FastAPI, Depends
from routers import users, stores

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "루트 경로"}

# 라우터
app.include_router(users.router)
app.include_router(stores.router)
