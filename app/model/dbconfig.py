from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import os
from dotenv import load_dotenv

load_dotenv()

data = {
    'name': 'mysql+pymysql',
    'user': 'admin',
    'pwd': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'port': '3306',
    'db': 'IntroToSe'
}

db_conn_string = f'{data["name"]}://' \
    f'{data["user"]}:{data["pwd"]}' \
    f'@{data["host"]}:{data["port"]}' \
    f'/{data["db"]}' \
    f'?charset=utf8'


class db_conn:
    def __init__(self):
        self.engine = create_engine(db_conn_string, pool_recycle=500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connect()
        return conn
