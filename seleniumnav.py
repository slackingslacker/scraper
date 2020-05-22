from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="geckodriver.exe")
print("navigate using driver")
driver.get("https://slackingslacker.github.io/selenium.html")
time.sleep(10)

el = driver.find_element_by_css_selector("#navigation > a")
print("navigate using HTML element")
el.click()
time.sleep(10)

print("navigate using javascript")
driver.execute_script("window.location.href='selenium.html';")
time.sleep(10)

el = driver.find_element_by_css_selector("#navigation > form")
print("navigate using submit form")
el.submit()
time.sleep(10)

print("navigate using forward button")
driver.forward()
time.sleep(10)

print("navigate using back button")
driver.back()
time.sleep(10)

driver.close()
