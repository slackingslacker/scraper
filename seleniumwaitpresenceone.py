from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex")

def wait_for_the_element(wait_time: int, el_id: str):
    try:
        print("[{}] Finding element {}".format(str(datetime.now()), el_id))
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_all_elements_located((By.ID, el_id))
        )
        print("[{}] Element found".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] Element did not load".format(str(datetime.now())))

wait_for_the_element(3, "navMenuId")
wait_for_the_element(6, "noneExistentId")
wait_for_the_element(9, "anotherNoneExistentId")
driver.close()
