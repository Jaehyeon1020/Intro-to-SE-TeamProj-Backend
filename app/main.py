from fastapi import FastAPI, Depends
from routers import users, stores
from dbconfig import session, User, Restaurant, Tag

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "루트 경로"}


@app.get("/db-connection-test")
async def test():
    # session.add(User(username="thisisusername", password="thisispassword"))
    # session.commit()
    restaurants = session.query(Restaurant).all()

    return {"result": restaurants}


# 라우터
app.include_router(users.router)
app.include_router(stores.router)
