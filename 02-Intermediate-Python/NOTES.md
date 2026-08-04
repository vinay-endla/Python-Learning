# Module 2 Notes

---

# 1. Modules

## What is a Module?

A module is simply a Python (.py) file.

Modules help organize large applications into smaller, reusable components.

Example:

billing.py

customers.py

main.py

---

## Import Entire Module

```python
import billing

billing.calculate_bill()
```

Preferred when using many functions.

---

## Module Alias

```python
import billing as bill
```

Examples:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

---

## Import Specific Functions

```python
from billing import calculate_bill
```

---

## Import Multiple Functions

```python
from billing import (
    calculate_bill,
    print_invoice,
)
```

---

## Function Alias

```python
from billing import (
    calculate_bill as calc_bill,
    print_invoice as invoice,
)
```

---

## Avoid

```python
from billing import *
```

Reason:

- Harder to read
- Possible naming conflicts

---

# 2. Variable Scope

## Global Scope

Variables created outside functions.

```python
customer = "John Smith"
```

---

## Local Scope

Variables created inside functions.

They exist only while the function executes.

---

## Variable Shadowing

A local variable hides a global variable with the same name.

---

## Parameters

Function parameters are local variables.

```python
def print_customer(customer):
```

---

## Scope Search Order

Python searches:

1. Local Scope
2. Global Scope

If not found:

```
NameError
```

---

## global Keyword

```python
global customer
```

Allows modification of a global variable.

Use sparingly.

---

# 3. Tuples

## What is a Tuple?

A tuple is an ordered, immutable collection.

```python
customer = (
    "John Smith",
    "MTR-001",
    842,
    True
)
```

---

## Tuple Indexing

```python
customer[0]
customer[1]
customer[-1]
```

Negative indexing starts from the end.

---

## Immutable

Tuples cannot be modified.

Invalid:

```python
customer[0] = "Mary"
```

Produces:

```
TypeError
```

---

## Tuple Unpacking

```python
name, meter, usage, solar = customer
```

Python assigns each tuple value to a variable.

---

## Extended Unpacking

```python
first, *rest = customer
```

```python
*rest, last = customer
```

```python
first, *middle, last = customer
```

The starred variable always becomes a **list**.

---

## Nested Unpacking

```python
customer = (
    "John",
    ("MTR-001", 842),
    True
)

name, (meter, usage), solar = customer
```

---

## Packing

Python automatically packs values into tuples.

Example:

```python
a = 10
b = 20

a, b = b, a
```

Conceptually:

```python
a, b = (b, a)
```

followed by tuple unpacking.

---

## Common Error

```python
name, meter = customer
```

Error:

```
ValueError:
too many values to unpack
```

Reason:

The number of variables must match the number of values unless using `*`.

---

## Where Tuple Unpacking Appears

```python
zip()
```

```python
enumerate()
```

```python
dict.items()
```

These all return tuples that Python unpacks automatically.

---

# 4. Sets

## What is a Set?

A set is an unordered, mutable collection of unique values.

```python
customers = {
    "John",
    "Mary",
    "David"
}
```

---

## Properties

- Unordered
- Mutable
- Stores unique values
- No indexing

---

## Creating Sets

```python
customers = {
    "John",
    "Mary"
}
```

or

```python
customers = set()
```

---

## Empty Set

```python
{}
```

Creates a dictionary.

```python
set()
```

Creates an empty set.

---

## Remove Duplicates

```python
meters = [
    "MTR-001",
    "MTR-002",
    "MTR-001"
]

unique = set(meters)
```

Result:

```
{
    "MTR-001",
    "MTR-002"
}
```

---

## Membership Testing

```python
"John" in customers
```

Returns True or False.

---

## Add

```python
customers.add("Sarah")
```

Duplicate values are ignored.

---

## Remove

```python
customers.remove("Mary")
```

Raises:

```
KeyError
```

if the element does not exist.

---

## Discard

```python
customers.discard("Mary")
```

Does nothing if the element is missing.

---

## Clear

```python
customers.clear()
```

Removes every element.

---

## Iteration

```python
for customer in customers:
    print(customer)
```

Sets cannot be indexed.

---

## Set Operations

### Union

```python
A | B
```

Everything from both sets.

Mathematics:

```
A ∪ B
```

---

### Intersection

```python
A & B
```

Common elements.

Mathematics:

```
A ∩ B
```

---

### Difference

```python
A - B
```

Elements in A but not in B.

---

### Symmetric Difference

```python
A ^ B
```

Elements that belong to exactly one set.

Equivalent to:

```
(A - B) ∪ (B - A)
```

---

## Professional Uses

- Remove duplicates
- Fast membership testing
- Compare datasets
- Find common records
- Find missing records
- Data analysis
- AI preprocessing
