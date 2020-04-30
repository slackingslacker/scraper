from bs4 import BeautifulSoup
import requests
url = "https://slackingslacker.github.io/simple.html"
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, "html.parser")
print(soup.find(id="d").text)
print(soup.find(id="p").text)