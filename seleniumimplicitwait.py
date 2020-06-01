from selenium import webdriver
from datetime import datetime

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.implicitly_wait(5)
driver.get("https://slackingslacker.github.io/seleniumindex")

def find_the_element(selector: str):
    try:
        print("[{}] Finding element {}".format(str(datetime.now()), selector))
        driver.find_element_by_css_selector(selector)
        print("[{}] Element found".format(str(datetime.now())))
    except Exception as e:
        print("[{}] Error is {}".format(str(datetime.now()), str(e)))

find_the_element("nav[role='navigation']")
find_the_element("#noneExistentId")
find_the_element("#anotherNoneExistentId")
driver.close()
