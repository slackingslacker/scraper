from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex")
time.sleep(5)

el = driver.find_element_by_css_selector("div[class='navbar-start'] > a:last-of-type")
el.click()
time.sleep(10)

driver.close()
