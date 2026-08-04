customer = (
    "John Smith",
    "MTR-001",
    842,
    True
)

customer1 = {
   "John Smith",
   "MTR-001"
}

print(customer[0])
print(customer1)
# print(customer1[0])

customer = (
    "John Smith",
    "MTR-001",
    842,
    True
)

# customer[0] = "Mary Johnson" 
# print(customer)

customer = (
    "John Smith",
    "MTR-001",
    842,
    True
)

print(customer[0])
print(customer[1])
print(customer[-1])
print(len(customer))


print(customer[-2])
print(customer[-3])


# name, meter_number, usage, is_solar = customer
# name, meter_number = customer

# first, *middle, last = customer
beginning,*middle,secondLast, ending = customer

print(beginning)
print(ending)
print(middle)
print(secondLast)


customer = (
    "John Smith",
    ("MTR-001", 842),
    True
)

name, (meter, usage), solar = customer

print(name)
print(meter)
print(usage)
print(solar)

# This explains something you've already used!

# Remember this?

# for customer_index, (customer, usage, is_solar) in enumerate(
#     zip(customers, monthly_usage, solar_customers),
#     start=1
# ):

# When we learned this in Module 1, it looked like magic.

# Now it should make perfect sense.

# Let's see what happens.

# Step 1

# zip() returns:

# (
#     "John Smith",
#     842,
#     True
# )
# Step 2

# enumerate() wraps that tuple:

# (
#     1,
#     (
#         "John Smith",
#         842,
#         True
#     )
# )

# Now Python sees:

# customer_index, (customer, usage, is_solar)

# So it performs two levels of unpacking.

# First:

# customer_index = 1

# (customer, usage, is_solar) = (
#     "John Smith",
#     842,
#     True
# )

# Then:

# customer = "John Smith"
# usage = 842
# is_solar = True