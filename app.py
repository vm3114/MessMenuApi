import json
import pytz
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fastapi import FastAPI
from datetime import datetime


def update_menu(day):

    chrome_driver_path = "/usr/bin/chromedriver"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = f'https://www.ssms-pilani.in/{day}'
    driver.get(url)
    menu_data = {}
    try:
        meal_sections = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".flex.flex-col.justify-start.items-center.p-10.border-4.rounded-xl.text-white.border-textgreen\\/50"))
            )
        
        for section in meal_sections:
            title = section.find_element(By.TAG_NAME, "h1").text
            menu_items = section.find_elements(By.TAG_NAME, "h1")[1:]
            items_text = [item.text for item in menu_items]
            menu_data[title] = items_text

        with open(f'menus/{day}.json', 'w') as file:
            json.dump(menu_data, file)

    except Exception as e:
        with open(f'menus/{day}.json', 'w') as file:
            json.dump("", file)
        print(f"An error occurred: {e}")

    driver.quit()
    return menu_data


def get_menu(day):
    with open(f"menus/{day}.json", "r") as file:
        menu = json.load(file)
    return menu


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
    menu = update_menu(day)
    return menu


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