from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.execute_script("window.location.href='https://slackingslacker.github.io/seleniumindex#/about';")
time.sleep(10)

driver.close()
