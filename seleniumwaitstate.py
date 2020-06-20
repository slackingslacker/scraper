from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import time

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumwait")

def wait_for_state(wait_time: int, el):
    try:
        print("[{}] Waiting for stateless element".format(str(datetime.now())))
        WebDriverWait(driver, wait_time).until(EC.staleness_of(el))
        print("[{}] Element stateless".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] Element exists".format(str(datetime.now())))

clickable_link = driver.find_element_by_css_selector("#elementStateless > a")
wait_for_state(3, clickable_link)
clickable_link.click()
time.sleep(5)
wait_for_state(6, clickable_link)
driver.quit()
