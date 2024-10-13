import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def add_response_code(data, code):
    return {"response_code": code, "result":data}


def update_menu(day):

    chrome_driver_path = "/usr/bin/chromedriver"
    chrome_options = Options()

    chrome_options.add_argument("--headless")  # Run headless
    chrome_options.add_argument("--no-sandbox")  # Disable sandboxing
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service,options=chrome_options)

    url = f'https://www.ssms-pilani.in/{day.lower()}'
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

        with open(f'menus/{day.lower()}.json', 'w') as file:
            json.dump(menu_data, file)
        
        response_code = 0

    except Exception as e:
        with open(f'menus/{day.lower()}.json', 'w') as file:
            json.dump("", file)
        print(f"An error occurred: {e}")
        response_code = 1


    driver.quit()
    return add_response_code(menu_data, response_code)



def get_menu(day):

    with open(f"menus/{day.lower()}.json", "r") as file:
        menu = json.load(file)
    
    if menu == "":
        response_code = 1
        menu = {}
        
    else:
        response_code = 0

    return add_response_code(menu, response_code)

