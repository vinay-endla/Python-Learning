# Variables in Python
name = "Vinay Kumar Endla"
experience = 15
company = "Oracle"
domain = "Oracle Utilities"
goal = "AI for Electric Utilities"

# This is a comment
print(f"My name is {name}")
print(f"I work at {company}")
print(f"I have {experience} years of experience.")
print(f"My domain is {domain}")
print(f"My long-term goal is {goal}")

# Customer Information
customer_name = "John Smith"
meter_id = "MTR100245"
city = "Philadelphia"
monthly_usage = 842
bill_amount = 126.35
solar_customer = True

# print the type of data
print(type(customer_name))
print(type(monthly_usage))
print(type(bill_amount))
print(type(solar_customer))

# Reassigning a variable
experience = 16
print(f"Updated experience: {experience}")

# Variables can change type
age = 30
age = "thirty"
print(f"Age variable now holds: {age}")

# Assigning multiple variables at once
x, y, z = 10, 20, 30
print(f"x = {x}, y = {y}, z = {z}")

# Using variables in arithmetic
a = 5
b = 3
sum_value = a + b
difference = a - b
product = a * b
quotient = a / b
print(f"Sum: {sum_value}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")

# Getting input from the user
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# Converting one type to another
num_str = "42"
num_int = int(num_str)
print(f"Converted value: {num_int + 8}")

# Naming rules
# Valid names: my_name, age2, total_count
# Invalid names: 2name, my-name

# Different variable types
text_message = "Hello, Python!"   # string
count = 7                          # integer
is_active = True                   # boolean
price = 19.99                      # float

print(f"Text: {text_message}")
print(f"Count: {count}")
print(f"Active: {is_active}")
print(f"Price: {price}")

# Simple practice exercise
favorite_food = "pizza"
favorite_color = "blue"
print(f"My favorite food is {favorite_food} and my favorite color is {favorite_color}.")
