customers = [
    {
        "name": "John Smith",
        "meter_number": "MTR-001",
        "monthly_usage": 842,
        "is_solar_customer": True
    },
    {
        "name": "Mary Johnson",
        "meter_number": "MTR-002",
        "monthly_usage": 1200,
        "is_solar_customer": False
    },
    {
        "name": "David Lee",
        "meter_number": "MTR-003",
        "monthly_usage": 430,
        "is_solar_customer": True
    },
    {
        "name": "Sarah Brown",
        "meter_number": "MTR-004",
        "monthly_usage": 1800,
        "is_solar_customer": False
    }
]

for customer in customers:
    # print(f"Name: {customer['name']}")    
    # print(f"Monthly Usage: {customer['monthly_usage']}")
    # print(
    # f"Is Solar Customer: "
    # f"{'Yes' if customer['is_solar_customer'] else 'No'}"
    # )
    print()
    # print(customer.get("name"))
    # print(customer["phone"]) #returns Key Error if key doesn't exist
    # print(customer.get("phone")) # returns None if key doesn't exist
    # print(customer.get("phone", "Not Available")) #returns default value if key doesn't exist
    # print(customer.keys())
    for key in customer.keys():
        print(f"{key}: {customer[key]}")
    for key, value in customer.items():
        print(f"{key}: {value}")


# | Method     | Returns                  | Example                          |
# | ---------- | ------------------------ | -------------------------------- |
# | `get()`    | One value (safe lookup)  | `customer.get("name")`           |
# | `keys()`   | All keys                 | `"name"`, `"meter_number"`...    |
# | `values()` | All values               | `"John Smith"`, `842`, `True`... |
# | `items()`  | Key-value pairs (tuples) | `("name", "John Smith")`         |
