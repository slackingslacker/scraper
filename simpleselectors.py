from bs4 import BeautifulSoup
import requests

url = "https://slackingslacker.github.io/simpleselectors.html"
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, "html.parser")


def find_by_selector(selector: str):
    elements = soup.select(selector)
    for el in elements:
        print("============================")
        print("name : " + el.name)
        print("attributes : " + str(el.attrs))
        print(el)

# finding tags based on CSS class column
find_by_selector(".column")

# finding tags with both CSS class in its attribute
find_by_selector(".table.is-narrow")

# finding the tags with columns class then find child elements
# with table class
find_by_selector(".columns .table")

# finding tag with id total
find_by_selector("#total")

# finding all div tags
find_by_selector("div")

# finding all div tags
find_by_selector("td.has-text-link")

# finding b and i tags
find_by_selector("b,i")

# finding all th under a table tag
find_by_selector("table th")

# finding all span which is direct child of div
find_by_selector("div > span")

# finding all p which is preceded by span
find_by_selector("span~p")

# finding tags with colspan attribute
find_by_selector("[colspan]")

# finding tags with colspan attribute that has a value of 2
find_by_selector("[colspan='2']")

# finding tags with class value that starts with has
find_by_selector("[class^='has']")

# finding tags with class value that ends with link
find_by_selector("[class$='link']")

# finding tags with class value that contains the word text
find_by_selector("[class*='text']")

# finding span tags that are empty
find_by_selector("span:empty")

# finding all first tr of the table tags
find_by_selector("tr:first-child")

# finding all last tr of the table tags
find_by_selector("tr:last-child")

# finding all the third td column of a tr (third child)
find_by_selector("td:nth-child(3)")

# finding all anchor tags that is the first child of the parent tag
find_by_selector("a:first-of-type")

# finding all anchor tags that is the last child of the parent tag
find_by_selector("a:last-of-type")

# finding all anchor tags that is the nth child of the parent tag
find_by_selector("a:nth-of-type(2)")

# finding all span tags is the only child
find_by_selector("span:only-child")

# finding specific tag using combination
find_by_selector("div.column:nth-of-type(1) > table > tr:nth-child(4) > td:nth-child(2)")

# finding specific tag using combination and displaying text
print(soup.select_one("div.column:nth-of-type(1) > table > tr:nth-child(4) > td:nth-child(2)").text)
