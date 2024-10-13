import pytz
import time
from functions import get_menu, update_menu, add_response_code
from fastapi import FastAPI, Request
from datetime import datetime,timedelta
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
err_response = {"response_code":2,"result":{}}  # usually for undefined query


@app.get("/doc", response_class=HTMLResponse)
async def read_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/get")   # /get for today, /get?day=monday for monday, /get?day=tomorrow for tomorrow
def get(day: str = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%A").lower()):

    dtime_today = datetime.now(pytz.timezone("Asia/Kolkata"))
    dtime_tmrw = dtime_today + timedelta(days=1)
    tomorrow = dtime_tmrw.strftime("%A").lower()

    if day.lower() == "tomorrow":
        day = tomorrow
    elif day.lower() in days_of_week:
        day = day.lower()
    else:
        return err_response
    
    print(f"Local time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
    print(f"PYTZ time: {dtime_today}")    
    return get_menu(day)


@app.get("/update")   # same as get
async def update(day: str = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%A").lower()):

    dtime_today = datetime.now(pytz.timezone("Asia/Kolkata"))
    dtime_tmrw = dtime_today + timedelta(days=1)
    tomorrow = dtime_tmrw.strftime("%A").lower()
    
    if day.lower() == "tomorrow":
        day = tomorrow
    elif day.lower() in days_of_week:
        day = day.lower()
    else:
        return err_response
    
    print(f"Local time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
    print(f"PYTZ time: {dtime_today}")    
    return update_menu(day)


@app.get("/updateall")
async def updateAll(start: str = "monday", end: str = "sunday"):  # /updateall for weekly menu, /updateall?start=tuesday&end=friday for menu on tue, wed, thu and fri
    try:   
        i = days_of_week.index(start.lower())
        end_index = days_of_week.index(end.lower())

    except:
        return err_response
    
    all_menu = {}
    while True:
        day = days_of_week[i]
        all_menu[day] = update_menu(day)

        if i == end_index:
            break
        else:
            i += 1
            i %= 7

    return all_menu


@app.get("/getall")
def getAll(start: str = "monday", end: str = "sunday"):  # same as updateall
    try:   
        i = days_of_week.index(start.lower())
        end_index = days_of_week.index(end.lower())

    except:
        return err_response
    
    all_menu = {}
    while True:
        day = days_of_week[i]
        all_menu[day] = get_menu(day)

        if i == end_index:
            break
        else:
            i += 1
            i %= 7
    
    return all_menu


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return RedirectResponse(url="/doc")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return RedirectResponse(url="/doc")