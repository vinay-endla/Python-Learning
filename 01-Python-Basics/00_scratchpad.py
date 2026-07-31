customers = [
    "John Smith",
    "Mary Johnson",
    "David Lee",
    "Sarah Brown"
]

monthly_usage = [
    842,
    1200,
    430,
    1800
]

solar_customers = [
    True,
    False,
    True,
    False
]

for customer_index in enumerate(
    zip(customers, monthly_usage, solar_customers),
    start=1
):
    print(customer_index[1][0])
    print(customer_index[1][1])
    print(customer_index[1][2])