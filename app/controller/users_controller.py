from fastapi import HTTPException
from model.users_dbhelper import users_dbhelper
from controller import dto

query = users_dbhelper()


def signup(id: str, password: str):
    return query.signup(id, password)


def logout():
    return query.logout()
