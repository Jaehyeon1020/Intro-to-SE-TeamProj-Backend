from fastapi import APIRouter
from dbconfig import session, User, Restaurant, Tag

router = APIRouter(prefix="/stores", tags=["stores"])


@router.get("/")
def get_all_stores():
    ''' 모든 식당 정보 반환 '''

    # DB에 존재하는 모든 식당 정보 가져오기
    restaurants = session.query(Restaurant).all()

    return restaurants


@router.get("/{store_id}")
def get_store_by_id(store_id: int):
    ''' id에 맞는 식당 정보 반환 '''

    # id에 맞는 식당 정보 찾기
    restaurant: Restaurant = session.query(
        Restaurant).filter_by(id=store_id).first()
    # 식당 id로 태그 정보 불러오기
    tag_info: Tag = session.query(Tag).filter_by(
        restaurant_id=restaurant.id).first()

    # 가장 많은 추천수를 가지는 태그 찾기(list)
    tags = {'1': tag_info.tag1, '2': tag_info.tag2, '3': tag_info.tag3,
            '4': tag_info.tag4, '5': tag_info.tag5, '6': tag_info.tag6, '7': tag_info.tag7}
    primary_tags = [k for k, v in tags.items() if max(tags.values()) == v]

    # 반환 정보
    restaurant_info = {"name": restaurant.restaurant_name, "address": restaurant.address,
                       "image_url": restaurant.image_url, "primary_tags": primary_tags}

    return restaurant_info


@router.get("/categories/{detail_category}")
def get_stores_by_category(detail_category: str):
    ''' 세부 카테고리에 맞는 가게 정보 반환 '''

    # 카테고리에 맞는 식당 정보 DB에서 가져오기
    restaurants = session.query(Restaurant).filter_by(
        category=detail_category).all()

    return restaurants


@router.get("/tags/{tag_number}")
def get_stores_by_tag(tag_number: int):
    ''' 태그 번호에 맞는 가게 정보 반환 '''
    pass


@router.get("/{store_id}/reviews")
def get_reviews_by_id(store_id: int):
    ''' id에 맞는 식당의 리뷰 반환 '''
    return {"store_id:": store_id}


@router.post("/{store_id}/reviews")
def create_new_review(store_id: int):
    ''' 새로운 리뷰 생성 '''
    return {"store_id": store_id}
