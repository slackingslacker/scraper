from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://www.google.com")
time.sleep(10)

driver.get("https://slackingslacker.github.io/seleniumindex")
time.sleep(10)

driver.close()
