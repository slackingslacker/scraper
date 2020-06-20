from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumwait")

def wait_for_window(wait_time: int, window_handles: list):
    try:
        print("[{}] Finding window".format(str(datetime.now())))
        WebDriverWait(driver, wait_time).until(EC.new_window_is_opened(window_handles))
        print("[{}] Window Opened".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] Window did not opened".format(str(datetime.now())))

handles = driver.window_handles
wait_for_window(3, handles)
driver.find_element_by_css_selector("#elementWindow > a").click()
wait_for_window(6, handles)
driver.quit()
