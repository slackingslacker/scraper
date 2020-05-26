from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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
    driver.get("https://slackingslacker.github.io/simple.html")
    logger.info("Finding #noneExistentId element")

    WebDriverWait(driver, 5).until(EC.title_is("Do It Simpler"))
    logger.info("Title found")
    WebDriverWait(driver, 3).until(EC.title_is("Do It SimplerS"))
except TimeoutException as e:
    logger.error(e)

try:
    logger.info("finding another element")
    WebDriverWait(driver, 7).until(EC.title_contains("Simpler"))
    logger.info("Title found")
    WebDriverWait(driver, 4).until(EC.title_contains("Simplers"))
except Exception as e:
    logger.error(e)

driver.close()
