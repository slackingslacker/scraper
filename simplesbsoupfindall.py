from bs4 import BeautifulSoup
import requests
import re

url = "https://slackingslacker.github.io/simpletags.html"
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, "html.parser")
# Will find all div tag elements
print(soup.find_all("div"))

# Will find all span and b tag elements
print(soup.find_all(["span", "b"]))

# Will find all tag elements starting with s
print(soup.find_all(re.compile("^s")))

# will find the text containing bold text
print(soup.find_all(string=re.compile("bold text")))

# will find all tag elements with id tableDiv
print(soup.find_all(id="tableDiv"))

# will find all tag element span and class red
print(soup.find_all("span", "red"))

# will find all tag elements with width of 400
print(soup.find_all(width="400"))

# will find all tag elements with combination
print(soup.find_all(width="400", height="100", border="1", id="secondTable"))

# will find all tag elements with limit
print(soup.find_all(name="table", width="400", limit=1))
print(soup.find_all(name="b", limit=2))

# will find all tag elements by css
print(soup.find_all(class_="red"))
print(soup.find_all(name="span", class_="red"))
print(soup.find_all(name=re.compile("^sp"), class_="red", string="span"))
print(soup.find_all(name="span", class_="black red-bg"))

# will find all tag elements using method as its filter
def with_specific(tag):
    return tag.has_attr("id") and tag.get("id", "") == "listDiv"
print(soup.find_all(with_specific))

# Will find all tag element
for tag in soup.find_all(True):
    print(tag.name)