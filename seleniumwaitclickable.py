from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumwait")

def wait_for_element_clickable(wait_time: int, id: str):
    try:
        print("[{}] Waiting clickable".format(str(datetime.now())))
        WebDriverWait(driver, wait_time).until(
            EC.element_to_be_clickable((By.ID, id))
        )
        print("[{}] Element clickable".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] Element not clickable".format(str(datetime.now())))

wait_for_element_clickable(3, "clickableBtn")
wait_for_element_clickable(6, "unclickableBtn")
driver.close()
