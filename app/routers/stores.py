from fastapi import APIRouter
from dbconfig import session, User, Restaurant, Tag


router = APIRouter(prefix="/stores", tags=["stores"])


@router.get("/")
def get_all_stores():
    ''' 모든 식당 정보 반환 '''
    restaurants = session.query(Restaurant).all()

    return restaurants


@router.get("/{store_id}")
def get_store_by_id(store_id: int):
    ''' id에 맞는 식당 정보 반환 '''
    restaurant = session.query(Restaurant).filter_by(id=store_id).first()

    return restaurant


@router.get("/{store_id}/reviews")
def get_reviews_by_id(store_id):
    ''' id에 맞는 식당의 리뷰 반환 '''
    return {"store_id:", store_id}


@router.post("/{store_id}/reviews")
def create_new_review(store_id):
    ''' 새로운 리뷰 생성 '''
    return {"store_id": store_id}
