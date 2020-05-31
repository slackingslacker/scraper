from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex")
time.sleep(3)
driver.get("https://slackingslacker.github.io/seleniumindex#/about")
time.sleep(3)

driver.back()
time.sleep(10)

driver.forward()
time.sleep(10)

driver.close()
