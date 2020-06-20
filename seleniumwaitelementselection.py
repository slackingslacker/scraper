from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumwait")

def wait_for_element_selection(wait_time: int, element, is_selected: bool):
    try:
        print("[{}] Waiting element".format(str(datetime.now())))
        WebDriverWait(driver, wait_time).until(
            EC.element_selection_state_to_be(element, is_selected)
        )
        print("[{}] Element found".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] Element not found".format(str(datetime.now())))

check_el = driver.find_element_by_css_selector("div#elementSelection input[name='forSelected']")
uncheck_el = driver.find_element_by_css_selector("div#elementSelection input[name='notSelected']")
option_el = driver.find_element_by_css_selector("div#elementSelection option[value='apple']")

wait_for_element_selection(3, check_el, True)
wait_for_element_selection(6, check_el, False)
wait_for_element_selection(9, uncheck_el, True)
wait_for_element_selection(12, uncheck_el, False)
wait_for_element_selection(15, option_el, True)
wait_for_element_selection(18, option_el, False)
driver.close()
