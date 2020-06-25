from selenium import webdriver

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumlocators")

elements = driver.find_elements_by_name("locatorName")
for el in elements:
    print(el.get_attribute("value"))
driver.quit()
