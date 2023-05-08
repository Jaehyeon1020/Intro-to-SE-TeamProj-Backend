from fastapi import APIRouter, Form
from pydantic import BaseModel
from controller import users_controller

router = APIRouter(prefix="/users", tags=["users"])
controller = users_controller


class User(BaseModel):
    id: str
    password: str


@router.post("/login")
def login(user: User):
    ''' 로그인 기능 구현 '''
    return "로그인"


@router.get("/logout")
def logout():
    ''' 로그아웃 기능 구현 '''
    return "로그아웃 api"


@router.post("/signup")
def signup(id: str = Form(), password: str = Form()):
    ''' 회원가입 기능 구현 '''
    user_form = {"id": id, "password": password}
    return user_form
