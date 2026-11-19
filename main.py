equipment_records = [
    {
        "item": "Computer",
        "supplier": "ABC Computers",
        "quantity": 10,
        "delivered": True
    },
    {
        "item": "Printer",
        "supplier": "XYZ Technologies",
        "quantity": 5,
        "delivered": False
    },
    {
        "item": "Scanner",
        "supplier": "ABC Computers",
        "quantity": 3,
        "delivered": False
    },
    {
    "item": "Monitor",
    "supplier": "Tech Solutions",
    "quantity": 8,
    "delivered": True
}
]
# 2. Display all equipment
def display_records(records):
    print("\n--- EQUIPMENT RECORDS ---")

    for record in records:
        print("Item:", record["item"])
        print("Supplier:", record["supplier"])
        print("Quantity:", record["quantity"])
        print("Delivered:", record["delivered"])
        print("------------------------")


# 3. Calculate total quantity
def calculate_total(records):
    total = 0

    for record in records:
        total = total + record["quantity"]

    return total


# 4. Find pending deliveries
def find_pending(records):
    pending = []

    for record in records:
        if record["delivered"] == False:
            pending.append(record)

    return pending

# 5. Main program
def main():
    display_records(equipment_records)

    total = calculate_total(equipment_records)

    print("\nTotal equipment quantity:", total)

    pending = find_pending(equipment_records)

    print("\n--- PENDING DELIVERIES ---")

    for item in pending:
        print(item["item"], "-", item["quantity"])


# Run program
if __name__ == "__main__":
    main()