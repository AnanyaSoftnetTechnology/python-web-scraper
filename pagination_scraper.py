
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

start_url = "https://books.toscrape.com/"
current_url = start_url

all_books = []
page_number = 1

try:
    while current_url:

        print(f"Scraping page {page_number}...")

        response = requests.get(current_url, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]

            price = book.find(
                "p", class_="price_color"
            ).get_text(strip=True)

            all_books.append({
                "Book Title": title,
                "Price": price
            })

        # Find the Next page link
        next_button = soup.find("li", class_="next")

        if next_button:
            next_link = next_button.a["href"]
            current_url = urljoin(current_url, next_link)
            page_number += 1
        else:
            current_url = None

    # Create DataFrame
   
    # Create DataFrame
    df = pd.DataFrame(all_books)
    print("Duplicate titles before cleaning:",
      df.duplicated(subset=["Book Title"]).sum())
    print("\nRecords before cleaning:", len(df))

    print("\nMissing values per column:")
    print(df.isnull().sum())

    print("\nRecords containing missing values:")
    print(df[df.isnull().any(axis=1)])

    print("\nDuplicate book records:")
    print(
    df[df.duplicated(subset=["Book Title"], keep=False)]
    .to_string(index=False)
    )   

    # Remove duplicate books
    df = df.drop_duplicates(subset=["Book Title"])

    # Remove missing values
    df = df.dropna()

    # Clean price and convert to numeric
    df["Price"] = (
        df["Price"]
        .str.replace("£", "", regex=False)
        .astype(float)
    )

    print("\n--- DATA QUALITY REPORT ---")
    print("Total records:", len(df))
    print("Duplicate records:", df["Book Title"].duplicated().sum())
    print("Missing values:", df.isnull().sum().sum())
    print("Average book price: £", round(df["Price"].mean(), 2))
    

    # Export files
    df.to_csv("all_books.csv", index=False, encoding="utf-8-sig")
    df.to_excel("all_books.xlsx", index=False)

    print("\n--- SCRAPING COMPLETED ---")
    print("Total pages scraped:", page_number)
    print("Total books collected:", len(df))
    print("\nFiles created successfully!")
except requests.exceptions.RequestException as error:
    print("Website connection failed:", error)

except Exception as error:
    print("Something went wrong:", error)