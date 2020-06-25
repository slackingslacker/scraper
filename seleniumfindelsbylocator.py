from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumlocators")

elements = driver.find_elements(By.CLASS_NAME, "is-medium")
for el in elements:
    print(el.text)
driver.quit()
