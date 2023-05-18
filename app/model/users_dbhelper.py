from .dbconfig import db_conn
from .schemas import User
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
import bcrypt
import jwt
import os
from datetime import datetime, timedelta

engine = db_conn()
session = engine.sessionmaker()


class users_dbhelper:
  def get_all_users(self):
    return session.query(User).all()

  def signup(self, id: str, password: str):
    exist_user: User = session.query(User).filter_by(username=id).first()

    if exist_user:
      raise HTTPException(status.HTTP_400_BAD_REQUEST, "이미 존재하는 사용자입니다.")

    hashed_pw = bcrypt.hashpw(password.encode(
        'utf-8'), bcrypt.gensalt()).decode('utf-8')
    new_user: User = User(username=id, password=hashed_pw)

    session.add(new_user)
    session.commit()

    return {"message": "새로운 사용자가 추가되었습니다."}

  def login(self, id: str, password: str):
    exist_user: User = session.query(User).filter_by(username=id).first()

    # id, pw 잘못되었으면 예외 발생
    if (not exist_user) or (not bcrypt.checkpw(password.encode('utf-8'), exist_user.password.encode('utf-8'))):
      raise HTTPException(status.HTTP_404_NOT_FOUND,
                          "아이디 또는 비밀번호를 확인 해주세요.")

    # id, pw 인증 후 jwt 토큰 발급
    payload = {"username": id, "exp": datetime.utcnow() +
               timedelta(minutes=30)}
    access_token = jwt.encode(
        payload, os.getenv("JWT_SECRET_KEY"), os.getenv("JWT_ALGORITHM"))

    # 응답 메세지 설정
    res = JSONResponse({"message": "로그인 성공"})

    # jwt 쿠키에 넣어서 전송
    res.set_cookie(key="access_token", value=access_token,
                   samesite='none', secure=True)

    return res

  def logout(self):
    # 응답 메세지 설정
    res = JSONResponse({"message": "로그아웃 성공"})

    # 설정되어있던 jwt 쿠키 내용 삭제
    res.set_cookie(key="access_token", value=None)

    return res

  def login_check(self, token: str):
    return token

    try:
      payload = jwt.decode(token, os.getenv(
          "JWT_SECRET_KEY"), os.getenv("JWT_ALGORITHM"))
    except:
      raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                          "로그인 상태가 아니거나 만료된 토큰입니다.")

    return {"message": payload["username"] + "님 로그인 상태입니다."}
