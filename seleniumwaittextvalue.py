from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumwait")

def wait_for_text(wait_time: int, selector: str, text_value: str):
    try:
        print("[{}] Finding text {}".format(str(datetime.now()), selector))
        WebDriverWait(driver, wait_time).until(
            EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, selector), text_value)
        )
        print("[{}] Text found".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] Text did not load".format(str(datetime.now())))

wait_for_text(3, "div#textExpectation > div:nth-of-type(1)", "This is an input")
wait_for_text(6, "div#textExpectation > div:nth-of-type(2) > input", "This is an input")
wait_for_text(9, "div#textExpectation > div:nth-of-type(1) > input", "this is an input")
driver.close()
