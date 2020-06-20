from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumwait")

def wait_for_element_selection(wait_time: int, selector: str, is_selected: bool):
    try:
        print("[{}] Waiting element {}".format(str(datetime.now()), selector))
        WebDriverWait(driver, wait_time).until(
            EC.element_located_selection_state_to_be((By.CSS_SELECTOR, selector), is_selected)
        )
        print("[{}] Element found".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] Element not found".format(str(datetime.now())))

wait_for_element_selection(3, "div#elementSelection input[name='forSelected']", True)
wait_for_element_selection(6, "div#elementSelection input[name='forSelected']", False)
wait_for_element_selection(9, "div#elementSelection input[name='notSelected']", True)
wait_for_element_selection(12, "div#elementSelection input[name='notSelected']", False)
wait_for_element_selection(15, "div#elementSelection option[value='apple']", True)
wait_for_element_selection(18, "div#elementSelection option[value='apple']", False)
driver.close()
