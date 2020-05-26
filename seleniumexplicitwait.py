from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s'))
logger.addHandler(handler)

driver = None
try:
    driver = webdriver.Firefox(executable_path="geckodriver.exe")
    logger.info("Going to website")
    driver.get("https://slackingslacker.github.io/simple.html")
    logger.info("Finding #noneExistentId element")

    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "noneExistentId"))
    )

except Exception as e:
    logger.error(e)

try:
    logger.info("finding another element")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "anotherNoneExistentId"))
    )
except Exception as e:
    logger.error(e)
    driver.close()
