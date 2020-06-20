from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumwait")

def wait_for_element_selected(wait_time: int, element):
    try:
        print("[{}] Waiting element".format(str(datetime.now())))
        WebDriverWait(driver, wait_time).until(
            EC.element_to_be_selected(element)
        )
        print("[{}] Element selected".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] Element not selected".format(str(datetime.now())))

check_el = driver.find_element_by_css_selector("div#elementSelected input[name='forSelectedRadio']")
uncheck_el = driver.find_element_by_css_selector("div#elementSelected input[name='notSelectedRadio']")

wait_for_element_selected(3, check_el)
wait_for_element_selected(6, uncheck_el)
driver.close()
