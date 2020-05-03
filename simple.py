import requests
url = "https://slackingslacker.github.io/simple.html"
print(requests.get(url).text)

url = "http://slackingslacker.pythonanywhere.com"
# Using GET Method
print(requests.get(url+"/get").text)
# Using POST Method
print(requests.post(url+"/post").text)
# Using PUT Method
print(requests.put(url+"/put").text)
# Using DELETE Method
print(requests.delete(url+"/delete").text)
# Using POST Method With FORM Submission
print(requests.post(url+"/postdata",
                    data={"name":"slackingslacker",
                          "location": "earth",
                          "height": "normal human"}).text)