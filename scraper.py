
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Website URL
url = "http://127.0.0.1:8000/sample_equipment.html"

# Step 2: Send HTTP request
response = requests.get(url, timeout=10)

# Check whether the request was successful
response.raise_for_status()

print("Website connected successfully!")

# Step 3: Read HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Find all equipment records
equipment_cards = soup.find_all(
    "div", class_="equipment-card"
)

equipment_records = []

# Step 5: Extract information
for card in equipment_cards:

    item = card.find("h2").get_text(strip=True)

    supplier = card.find(
        "p", class_="supplier"
    ).get_text(strip=True)

    quantity = int(
        card.find("p", class_="quantity").get_text(strip=True)
    )

    delivered = (
        card.find("p", class_="delivered")
        .get_text(strip=True)
        == "Yes"
    )

    record = {
        "Item": item,
        "Supplier": supplier,
        "Quantity": quantity,
        "Delivered": delivered
    }

    equipment_records.append(record)

# Step 6: Convert records into a DataFrame
df = pd.DataFrame(equipment_records)

# Step 7: Export to CSV
df.to_csv("equipment_records.csv", index=False)

# Step 8: Export to Excel
df.to_excel("equipment_records.xlsx", index=False)

# Step 9: Display results
print("\n--- SCRAPED EQUIPMENT RECORDS ---")
print(df.to_string(index=False))

print("\nTotal equipment quantity:", df["Quantity"].sum())

print("\nPending deliveries:")
print(df[df["Delivered"] == False].to_string(index=False))

print("\nCSV and Excel files created successfully!")
