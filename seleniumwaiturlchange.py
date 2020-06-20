from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
url = "https://slackingslacker.github.io/seleniumindex#/seleniumwait"
driver.get(url)

def wait_for_url_change(wait_time: int, expected_url: str):
    try:
        print("[{}] Current URL {}".format(str(datetime.now()), driver.current_url))
        WebDriverWait(driver, wait_time).until(
            EC.url_changes(expected_url)
        )
        print("[{}] URL changed".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] URL did not changed".format(str(datetime.now())))

wait_for_url_change(3, url)
clickable_link = driver.find_element_by_css_selector("#elementStateless > a")
clickable_link.click()
wait_for_url_change(6, url)
driver.close()
