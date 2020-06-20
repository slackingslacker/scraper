from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumwait")

def wait_for_url_contains(wait_time: int, text: str):
    try:
        print("[{}] URL contains {}".format(str(datetime.now()), text))
        WebDriverWait(driver, wait_time).until(
            EC.url_contains(text)
        )
        print("[{}] URL has text".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] URL does not contain text ".format(str(datetime.now())))

wait_for_url_contains(3, "seleniumindex")
wait_for_url_contains(6, "simple")
driver.close()
