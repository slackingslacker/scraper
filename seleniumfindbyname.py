from selenium import webdriver

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumlocator")

el = driver.find_element_by_name("locatorName")
print(el.get_attribute("value"))
driver.quit()
