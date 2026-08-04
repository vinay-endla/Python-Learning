# List Comprehension
# [
#     expression_if_true if condition else expression_if_false
#     for variable in iterable
# ]


monthly_usage = [842, 1200, 430, 1800]

usage_mwh = []

for usage in monthly_usage:
    usage_mwh.append(usage / 1000)

print(usage_mwh)

usage_mwh = [
    usage / 1000
    for usage in monthly_usage
]

print(usage_mwh)

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)

customers=["John Doe","Jane Smith","Bob Johnson"]
upper_names=[
    name.upper()
    for name in customers
]
print(upper_names)

monthly_usage = [842, 1200, 430, 1800]

high_usage = [
    usage
    for usage in monthly_usage
    if usage > 1000
]
print(high_usage)

numbers = [1, 2, 3, 4, 5, 6]

even_squares = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

print(even_squares)
usage_categories = [
    "High"
    if usage > 1000
    else "Normal"
    for usage in monthly_usage
]
print(usage_categories)