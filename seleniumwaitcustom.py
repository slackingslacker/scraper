from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from datetime import datetime


class has_text(object):
    """An expectation for checking that an element has a particular case insensitive text.

    locator - used to find the element
    returns the WebElement once it has the particular css class
    """


    def __init__(self, locator, text: str = ""):
        self.locator = locator
        self.text = text


    def __call__(self, driver):
        element = driver.find_element(*self.locator)  # Finding the referenced element
        if self.text.lower() == element.text.lower():
            return element
        else:
            return False


driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumwait")


def wait_for_text(wait_time: int, selector: str, text_value: str):
    try:
        print("[{}] Finding text {}".format(str(datetime.now()), selector))
        WebDriverWait(driver, wait_time).until(
            has_text((By.CSS_SELECTOR, selector), text_value)
        )
        print("[{}] Text found".format(str(datetime.now())))
    except TimeoutException as e:
        print("[{}] Text did not load".format(str(datetime.now())))


wait_for_text(3, "div#textExpectation > div:nth-of-type(1)", "Expected Text")
wait_for_text(6, "div#textExpectation > div:nth-of-type(2)", "Expected Text")
wait_for_text(9, "div#textExpectation > div:nth-of-type(1)", "expected text")
driver.close()
