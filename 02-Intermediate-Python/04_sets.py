customers = {
    "John Smith",
    "Mary Johnson",
    "David Lee",
    "Sarah Brown"
}

print(customers)

customers1 = [
    "John",
    "Mary",
    "David"
]


print(customers1)

customers = {
    "John Smith",
    "Mary Johnson",
    "David Lee",
    "Sarah Brown",
    "John Smith"
}

print(customers)
print(len(customers))

meters = [
    "MTR-001",
    "MTR-002",
    "MTR-001",
    "MTR-003",
    "MTR-002",
    "MTR-004"
]

unique_meters = set(meters)

print(unique_meters)
print(type(unique_meters))

customers.add("Sarah Brown")

print(customers)

customers.add("John Smith")

print(customers)

if "John Smith" in customers:
    print("Customer exists")

customers = {
    "John Smith",
    "Mary Johnson",
    "David Lee"
}

customers.remove("Mary Johnson")

print(customers)

# customers.remove("Vinay")
customers.discard("Vinay")

print(customers)

customers = {
    "John Smith",
    "Mary Johnson",
    "David Lee"
}

print("John Smith" in customers)
print("Vinay" in customers)

for customer in customers:
    print(customer)

customers.clear()

print(customers)
print(len(customers))

a = {}

b = set()

print(type(a))
print(type(b))

peco = {
    "John",
    "Mary",
    "David"
}

solar = {
    "Mary",
    "David",
    "Sarah"
}

print(peco | solar)
print(peco & solar)
print(peco - solar)
print(peco ^ solar)