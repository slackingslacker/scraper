from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumlocator")

el = driver.find_element(By.CSS_SELECTOR, "div#locatorCSSSelector")
print(el.text)
driver.quit()
