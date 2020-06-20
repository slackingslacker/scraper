from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumwait")

def wait_for_frame(wait_time: int, selector: str):
    try:
        print("[{}] Waiting for iframe {}".format(str(datetime.now()), selector))
        WebDriverWait(driver, wait_time).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, selector))
        )
        print("[{}] Frame Loaded".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] Frame did not load".format(str(datetime.now())))

wait_for_frame(3, "div#elementFrame iframe")
wait_for_frame(6, "div#elementFrames iframe")
driver.close()
