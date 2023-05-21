from .dbconfig import db_conn
from .schemas import Restaurant, Tag
from sqlalchemy import func
from fastapi import HTTPException

engine = db_conn()
session = engine.sessionmaker()


class stores_dbhelper:
  def create_store(self, restaurant_name, image_url, address, category):
    ''' 식당 추가 '''
    if session.query(Restaurant).filter_by(restaurant_name=restaurant_name).first():
      raise HTTPException(400, "이미 존재하는 식당입니다.")

    new_restaurant = Restaurant(restaurant_name=restaurant_name,
                                image_url=image_url, address=address, category=category)
    session.add(new_restaurant)
    session.commit()

    return "새로운 식당이 추가되었습니다."

  def get_all_stores(self):
    ''' 모든 식당 정보 반환 '''

    # DB에 존재하는 모든 식당 정보 가져오기
    restaurants = session.query(Restaurant).all()

    return restaurants

  def get_stores_by_id(self, store_id: int):

    restaurant: Restaurant = session.query(
        Restaurant).filter_by(id=store_id).first()

    tag_info: Tag = session.query(Tag).filter_by(
        restaurant_id=restaurant.id).first()

    tags = {'1': tag_info.tag1, '2': tag_info.tag2, '3': tag_info.tag3,
            '4': tag_info.tag4, '5': tag_info.tag5, '6': tag_info.tag6, '7': tag_info.tag7}
    primary_tags = [k for k, v in tags.items() if max(tags.values()) == v]

    # 반환 정보
    restaurant_info = {"name": restaurant.restaurant_name, "address": restaurant.address,
                       "image_url": restaurant.image_url, "primary_tags": primary_tags}

    return restaurant_info

  def get_stores_by_category(self, detail_category: str):
    ''' 세부 카테고리에 맞는 가게 정보 반환 '''

    # 카테고리에 맞는 식당 정보 DB에서 가져오기
    restaurants = session.query(Restaurant).where(
        Restaurant.category.contains(detail_category)).all()

    return restaurants

  def get_stores_by_tag(self, tag_number: int):
    ''' 태그 번호에 맞는 가게 정보 반환 '''

    tag_column = getattr(Tag, f"tag{tag_number}")

    restaurants = session.query(
        Restaurant
    ).join(
        Tag,
        Restaurant.id == Tag.restaurant_id
    ).order_by(tag_column.desc()).all()

    print(restaurants)

    return restaurants

  def get_reviews_by_id(self, store_id: int):
    ''' id에 맞는 식당의 리뷰 반환 '''

    restaurant = session.query(Tag).filter(
        Tag.restaurant_id == store_id
    ).all()

    return restaurant

  def create_new_review(self, store_id,
                        tag1, tag2, tag3, tag4, tag5, tag6, tag7):
    ''' 새로운 리뷰 생성  '''

    restaurant: Restaurant = session.query(
        Restaurant).filter(Restaurant.id == store_id).first()
    if not restaurant:
      raise HTTPException(
          status_code=404, detail=f"Restaurant with id {store_id} not found")

    tag_info: Tag = session.query(Tag).filter(
        Tag.restaurant_id == store_id).first()
    if not tag_info:
      raise HTTPException(
          status_code=404, detail=f"Tags for restaurant with id {store_id} not found")

    tag_data = {
        "tag1": tag1,
        "tag2": tag2,
        "tag3": tag3,
        "tag4": tag4,
        "tag5": tag5,
        "tag6": tag6,
        "tag7": tag7
    }

    for tag, value in tag_data.items():
      if value == 1:
        current_tag_value = getattr(tag_info, tag)
        setattr(tag_info, tag, current_tag_value + 1)

    session.commit()

  # def create_new_review(self, store_id: int, tags):
  #   ''' 새로운 리뷰 생성 '''

  #   restaurant: Restaurant = session.query(
  #       Restaurant).filter(Restaurant.id == store_id).first()
  #   if not restaurant:
  #     raise HTTPException(
  #         status_code=404, detail=f"Restaurant with id {store_id} not found")

  #   tag_info: Tag = session.query(Tag).filter(
  #       Tag.restaurant_id == store_id).first()
  #   if not tag_info:
  #     raise HTTPException(
  #         status_code=404, detail=f"Tags for restaurant with id {store_id} not found")

  #   for tag in tags:
  #     current_tag_value = getattr(tag_info, f"{tag}")
  #     setattr(tag_info, f"{tag}", current_tag_value + 1)

  #   session.commit()
