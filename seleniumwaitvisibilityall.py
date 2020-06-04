from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/divtags")

def wait_for_the_elements(wait_time: int, selector: str):
    try:
        print("[{}] Finding element {}".format(str(datetime.now()), selector))
        WebDriverWait(driver, wait_time).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector)))
        print("[{}] Element found".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] Element did not load".format(str(datetime.now())))

wait_for_the_elements(3, "div#hiddenElements > div:nth-of-type(3)")
wait_for_the_elements(6, "div#hiddenElements > div:nth-of-type(1)")
wait_for_the_elements(9, "div#hiddenElements > div:nth-of-type(2)")
wait_for_the_elements(12, "div#hiddenElements > div")
driver.close()
