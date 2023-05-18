from sqlalchemy import Column, ForeignKey, Boolean, Text
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

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
  image_url = Column(String(450), nullable=False)
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
