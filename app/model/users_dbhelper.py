from model.dbconfig import db_conn
from model.schemas import User

engine = db_conn()
session = engine.sessionmaker()


class users_dbhelper:
    def logout(self):
        return {"users": "check"}
