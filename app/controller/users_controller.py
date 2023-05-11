from fastapi import HTTPException
from ..model.users_dbhelper import users_dbhelper
from . import dto

query = users_dbhelper()


def get_all_users():
    return query.get_all_users()


def signup(id: str, password: str):
    return query.signup(id, password)


def login(id: str, password: str):
    return query.login(id, password)


def logout():
    return query.logout()


def login_check(token: str):
    return query.login_check(token)
