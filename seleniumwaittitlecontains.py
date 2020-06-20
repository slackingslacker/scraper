from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex")

def wait_for_the_title(wait_time: int, doc_title: str):
    try:
        print("[{}] Waiting for title {}".format(str(datetime.now()), doc_title))
        WebDriverWait(driver, wait_time).until(EC.title_contains(doc_title))
        print("[{}] Title found".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] Error waiting for title".format(str(datetime.now())))

wait_for_the_title(3, "Do It Simpler")
wait_for_the_title(6, "Not the title")
wait_for_the_title(9, "do it simpler")
driver.close()
