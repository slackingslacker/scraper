from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumwait")

def wait_for_element_selected(wait_time: int, selector: str):
    try:
        print("[{}] Waiting element {}".format(str(datetime.now()), selector))
        WebDriverWait(driver, wait_time).until(
            EC.element_located_to_be_selected((By.CSS_SELECTOR, selector))
        )
        print("[{}] Element selected".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] Element not selected".format(str(datetime.now())))

wait_for_element_selected(3, "div#elementSelected input[name='forSelectedRadio']")
wait_for_element_selected(6, "div#elementSelected input[name='notSelectedRadio']")
driver.close()
