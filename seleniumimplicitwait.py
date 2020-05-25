from selenium import webdriver
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
    driver.implicitly_wait(5)
    logger.info("Going to website")
    driver.get("https://slackingslacker.github.io/simple.html")
    logger.info("Finding #noneExistentId element")
    driver.find_element_by_css_selector("#noneExistentId")
except Exception as e:
    logger.error(str(e))

try:
    logger.info("finding another element")
    driver.find_element_by_css_selector("#anotherNoneExistentId")
except Exception as e:
    logger.error(str(e))
    driver.close()
