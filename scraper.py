import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

response = requests.get(url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []

for book in books:

    title = book.h3.a["title"]

    price = book.find(
        "p", class_="price_color"
    ).text.strip()

    availability = book.find(
        "p", class_="instock availability"
    ).text.strip()

    rating_class = book.find(
        "p", class_="star-rating"
    )["class"]

    rating = rating_class[1]

    data.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Availability": availability
    })

df = pd.DataFrame(data)

df.to_csv("books_data.csv", index=False, encoding="utf-8-sig")

print("Scraping completed successfully!")
print("Total books collected:", len(df))
print("Dataset saved as books_data.csv")