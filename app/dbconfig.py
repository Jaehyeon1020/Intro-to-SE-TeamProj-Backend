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

Base = declarative_base()


class User(Base):
  # 이 클래스로 user 테이블에 들어갈 유저 객체 생성 가능
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(200), nullable=False)


class Restaurant(Base):
  # 이 클래스로 restaurant 테이블에 들어갈 유저 객체 생성 가능
    __tablename__ = "restaurant"

    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String(50), nullable=False)
    image_url = Column(String(200), nullable=False)
    address = Column(String(100), nullable=False)
    category = Column(String(30), nullable=False)


class Tag(Base):
  # 이 클래스로 tag 테이블에 들어갈 유저 객체 생성 가능
    __tablename__ = "tag"

    restaurant_id = Column(Integer, primary_key=True)
    tag1 = Column(Integer, nullable=False)
    tag2 = Column(Integer, nullable=False)
    tag3 = Column(Integer, nullable=False)
    tag4 = Column(Integer, nullable=False)
    tag5 = Column(Integer, nullable=False)
    tag6 = Column(Integer, nullable=False)
    tag7 = Column(Integer, nullable=False)


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


db = db_conn()
conn = db.connection()
session = db.sessionmaker()
