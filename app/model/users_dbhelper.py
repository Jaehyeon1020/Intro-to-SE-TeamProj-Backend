from model.dbconfig import db_conn
from model.schemas import User
from fastapi import HTTPException, status
import bcrypt

engine = db_conn()
session = engine.sessionmaker()


class users_dbhelper:
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

    def logout(self):
        return {"users": "check"}
