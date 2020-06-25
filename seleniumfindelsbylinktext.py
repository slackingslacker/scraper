from selenium import webdriver

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumlocators")

elements = driver.find_elements_by_link_text("This is for locator LINK TEXT")
for el in elements:
    print(el.text)
driver.quit()
