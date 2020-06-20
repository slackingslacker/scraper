from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumwait")

def wait_for_window(wait_time: int, window_nums: int):
    try:
        print("[{}] Finding window".format(str(datetime.now())))
        WebDriverWait(driver, wait_time).until(EC.number_of_windows_to_be(window_nums))
        print("[{}] Window Opened is {}".format(str(datetime.now()), str(window_nums)))
    except TimeoutException as e:
        print("[{}] Window did not opened".format(str(datetime.now())))

wait_for_window(3, 2)
driver.find_element_by_css_selector("#elementWindow > a").click()
wait_for_window(6, 2)
driver.quit()
