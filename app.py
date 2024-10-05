from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():

    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    driver = webdriver.Chrome(options=chrome_options)

    url = f'https://www.ssms-pilani.in/{datetime.today().strftime("%A").lower()}'
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

    except Exception as e:
        print(f"An error occurred: {e}")

    driver.quit()

    return menu_data