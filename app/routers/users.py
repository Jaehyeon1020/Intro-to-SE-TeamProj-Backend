from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])


class User(BaseModel):
    id: str
    password: str


@router.post("/login")
def login(user: User):
    ''' 로그인 기능 구현 '''
    return "로그인 api"


@router.get("/logout")
def logout():
    ''' 로그아웃 기능 구현 '''
    return "로그아웃 api"


@router.post("/signup")
def signup(user: User):
    ''' 회원가입 기능 구현 '''
    return "회원가입 api"
