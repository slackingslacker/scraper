from selenium import webdriver

driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://slackingslacker.github.io/seleniumindex#/seleniumlocators")

elements = driver.find_elements_by_css_selector("div#locatorCSSSelector")
for el in elements:
    print(el.text)
driver.quit()
