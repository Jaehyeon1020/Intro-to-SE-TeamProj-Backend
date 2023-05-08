from fastapi import APIRouter
from controller import stores_controller

router = APIRouter(prefix="/stores", tags=["stores"])
controller = stores_controller


@router.get("/")
def get_all_stores():
    ''' 모든 식당 정보 반환 '''

    response = controller.get_all_stores()

    return response


@router.get("/{store_id}")
def get_store_by_id(store_id: int):
    ''' id에 맞는 식당 정보 반환 '''

    response = controller.get_store_by_id(store_id)

    return response


@router.get("/categories/{detail_category}")
def get_stores_by_category(detail_category: str):
    ''' 세부 카테고리에 맞는 가게 정보 반환 '''

    response = controller.get_stores_by_category(detail_category)

    return response


@router.get("/tags/{tag_number}")
def get_stores_by_tag(tag_number: int):
    ''' 태그 번호에 맞는 가게 정보 반환 '''

    response = controller.get_stores_by_tag(tag_number)

    return response


@router.get("/{store_id}/reviews")
def get_reviews_by_id(store_id: int):
    ''' id에 맞는 식당의 리뷰 반환 '''
    return {"store_id:": store_id}


@router.post("/{store_id}/reviews")
def create_new_review(store_id: int):
    ''' 새로운 리뷰 생성 '''
    return {"store_id": store_id}
