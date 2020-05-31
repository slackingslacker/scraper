from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex")
time.sleep(5)
driver.close()

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex")
time.sleep(5)
driver.close()
