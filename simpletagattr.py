from bs4 import BeautifulSoup
import requests
url = "https://slackingslacker.github.io/simpletags.html"
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, "html.parser")
print(soup.find(id="hDiv").name)
image_tag = soup.find(id="imgId")
print(image_tag["src"])
print(image_tag["width"])
print(image_tag["height"])
print(image_tag["alt"])