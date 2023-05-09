from fastapi import APIRouter, Form, Cookie
from pydantic import BaseModel
from controller import users_controller

router = APIRouter(prefix="/users", tags=["users"])
controller = users_controller


class User(BaseModel):
    id: str
    password: str


@router.get("/")
def get_all_users():
    ''' (테스트용) 모든 유저 정보 가져오기 '''
    return controller.get_all_users()


@router.post("/login")
def login(id: str = Form(), password: str = Form()):
    ''' 로그인 기능 구현 '''
    return controller.login(id, password)


@router.get("/logout")
def logout():
    ''' 로그아웃 기능 구현 '''
    return controller.logout()


@router.post("/signup")
def signup(id: str = Form(), password: str = Form()):
    ''' 회원가입 기능 구현 '''
    return controller.signup(id, password)


@router.get("/logincheck")
def login_check(access_token=Cookie(None)):
    return controller.login_check(access_token)
