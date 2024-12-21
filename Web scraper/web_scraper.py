import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article")

for book in books :
    title = book.h3.a["title"]
    rating = book.p["class"][1]
    price = book.find("p" , class_="price_color")
    print(f"the book title is : {title} and it's price is : {price.text} and  it's rate is : {rating} stars")




