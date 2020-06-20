from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumwait")

def wait_for_alert(wait_time: int):
    try:
        print("[{}] Waiting for alert".format(str(datetime.now())))
        WebDriverWait(driver, wait_time).until(EC.alert_is_present())
        print("[{}] Alert found".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] Alert did not load".format(str(datetime.now())))

wait_for_alert(3)
driver.find_element_by_css_selector("#alertExpectation button").click()
wait_for_alert(6)
driver.quit()
