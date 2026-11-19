
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    print("Website connected successfully!")

    # Parse webpage content with correct character encoding
    soup = BeautifulSoup(response.content, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    book_records = []

    for book in books:
        title = book.h3.a["title"]
        price = book.find(
            "p", class_="price_color"
        ).get_text(strip=True)

        book_records.append({
            "Book Title": title,
            "Price": price
        })

    # Convert records into a DataFrame
    df = pd.DataFrame(book_records)

    print("\n--- BOOK DETAILS ---")
    print(df.to_string(index=False))

    print("\nTotal books found:", len(df))

    # Export data
    df.to_csv("books_data.csv", index=False, encoding="utf-8-sig")
    df.to_excel("books_data.xlsx", index=False)

    print("\nCSV and Excel files created successfully!")

except requests.exceptions.RequestException as error:
    print("Website connection failed:", error)

except Exception as error:
    print("Something went wrong:", error)
