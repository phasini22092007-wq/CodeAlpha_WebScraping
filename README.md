# CodeAlpha Web Scraping Project

## Project Title

Web Scraping of Travel Books Dataset

## Objective

The objective of this project is to use Python web scraping libraries to collect useful information from a public website and create a structured dataset for further analysis.

## Website Used

Books to Scrape – Travel Category

https://books.toscrape.com/catalogue/category/books/travel_2/index.html

## Data Collected

The following information was extracted from the website:

* Title
* Price
* Rating
* Availability

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas
* VS Code

## How the Project Works

1. Python Requests sends a request to the website.
2. BeautifulSoup reads and parses the HTML content.
3. The required book information is extracted.
4. Pandas stores the extracted information in a structured dataset.
5. The dataset is saved as `books_data.csv`.

## Output

The scraper collected 11 books from the Travel category.

The final dataset is stored in:

`books_data.csv`

## Files in the Project

* `scraper.py` – Python web scraping program
* `books_data.csv` – Scraped dataset
* `requirements.txt` – Required Python libraries
* `README.md` – Project documentation

## Conclusion

This project demonstrates how Python can be used to extract data from a public webpage and convert it into a structured CSV dataset that can be used for further data analysis.
