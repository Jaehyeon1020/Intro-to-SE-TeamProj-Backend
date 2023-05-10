from fastapi import HTTPException
from model.stores_dbhelper import stores_dbhelper
from controller import dto

query = stores_dbhelper()


def get_all_stores():
    ''' 모든 식당 정보 반환 '''

    restaurants = query.get_all_stores()

    response = dto.to_json(restaurants)

    return response


def get_store_by_id(store_id: int):
    ''' id에 맞는 식당 정보 반환 '''

    restaurant_info = query.get_stores_by_id(store_id)

    response = dto.to_json(restaurant_info)

    return response


def get_stores_by_category(detail_category: str):
    ''' 세부 카테고리에 맞는 가게 정보 반환 '''

    restaurants = query.get_stores_by_category(detail_category)

    response = dto.to_json(restaurants)

    return response


def get_stores_by_tag(tag_number: int):
    ''' 태그 번호에 맞는 가게 정보 반환 '''

    restaurants = query.get_stores_by_tag(tag_number)

    response = restaurants  # dto.to_json(restaurants)

    return response


def get_reviews_by_id(store_id: int):
    ''' id에 맞는 식당의 리뷰 반환 '''

    restaurant = query.get_reviews_by_id(store_id)

    response = dto.to_json(restaurant)

    return response


def create_new_review(store_id: int, tags):
    ''' 새로운 리뷰 생성 '''
    query.create_new_review(store_id, tags)
