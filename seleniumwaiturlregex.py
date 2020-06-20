from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
url = "https://slackingslacker.github.io/seleniumindex#/seleniumwait"
driver.get(url)

def wait_for_url_matches(wait_time: int, matcher_re: str):
    try:
        print("[{}] Matcher regex {}".format(str(datetime.now()), matcher_re))
        WebDriverWait(driver, wait_time).until(
            EC.url_matches(matcher_re)
        )
        print("[{}] URL contains".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] URL does not contain".format(str(datetime.now())))

wait_for_url_matches(3, "[^a-zA-Z0-9]")
wait_for_url_matches(6, "[0-9]")
driver.close()
