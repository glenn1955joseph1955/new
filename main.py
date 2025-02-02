from fastapi import FastAPI
from fastapi.responses import RedirectResponse, PlainTextResponse
import pymysql
import pymysql.cursors
from config import host, user, password, db_name
import requests


app = FastAPI()

@app.get("/")
def new():
    return RedirectResponse('https://poshmark21.com')

