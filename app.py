import pytz
from functions import get_menu, update_menu, add_response_code
from fastapi import FastAPI
from datetime import datetime


app = FastAPI()
timezone = pytz.timezone("Asia/Kolkata")
today = datetime.now(timezone).strftime("%A").lower()
days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


@app.get("/get")
@app.get("/get/{day}")
def get_today(day: str = today):
    return get_menu(day)


@app.get("/update")
@app.get("/update/{day}")
async def update_today(day: str = today):
    return update_menu(day)


@app.get("/updateall")
async def updateAll():
    all_menu = {}
    for day in days_of_week:
        menu = update_menu(day)
        all_menu[day] = menu
    return all_menu


@app.get("/getall")
def getAll():
    all_menu = {}
    for day in days_of_week:
        menu = get_menu(day)
        all_menu[day] = menu
    return all_menu