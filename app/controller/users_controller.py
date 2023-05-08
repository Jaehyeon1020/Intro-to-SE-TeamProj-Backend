from fastapi import HTTPException
from model.users_dbhelper import users_dbhelper
from controller import dto

query = users_dbhelper()


def logout():
    return query.logout()
