import requests
url = "https://slackingslacker.github.io/simple.html"
print(requests.get(url).text)