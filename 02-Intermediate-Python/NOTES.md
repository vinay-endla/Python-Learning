# Module 2 Notes

---

# 1. Modules

A module is simply a Python (.py) file.

Modules help organize applications into reusable components.

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

Preferred when using many functions from the same module.

---

## Module Alias

```python
import billing as bill

bill.calculate_bill()
```

Common for long module names.

Examples:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

---

## Import Specific Function

```python
from billing import calculate_bill

calculate_bill()
```

Useful when importing only one or two functions.

---

## Import Multiple Functions

```python
from billing import (
    calculate_bill,
    print_invoice,
)
```

---

## Function Aliases

```python
from billing import (
    calculate_bill as calc_bill,
    print_invoice as invoice,
)
```

Useful for readability and avoiding naming conflicts.

---

## Avoid

```python
from billing import *
```

Reason:

- Imports everything
- Can create name collisions
- Makes code harder to understand

---

# 2. Variable Scope

---

## Global Scope

Variables created outside functions.

```python
customer = "John Smith"
```

Accessible throughout the module unless shadowed.

---

## Local Scope

Variables created inside functions.

```python
def update_customer():
    customer = "Mary Johnson"
```

Exist only while the function is executing.

After the function finishes, they are destroyed.

---

## Variable Shadowing

A local variable with the same name as a global variable temporarily hides the global variable inside that function.

```python
customer = "John"

def func():
    customer = "Mary"
```

Inside `func()`, Python uses `"Mary"`.

Outside, Python still uses `"John"`.

---

## Scope Search Order

Python looks for variables in this order:

1. Local scope
2. Global scope

If not found:

```
NameError
```

---

## Parameters Create Local Variables

```python
def print_customer(customer):
    print(customer)
```

The parameter `customer` is a local variable.

Every function call gets its own local scope.

---

## Each Function Has Its Own Local Scope

Functions cannot access another function's local variables.

Each function receives only:

- Its own local variables
- Global variables

---

## global Keyword

```python
customer = "John"

def update():
    global customer
    customer = "Mary"
```

The `global` keyword tells Python to modify the global variable instead of creating a local one.

---

## Professional Recommendation

Prefer passing data through parameters and returning results.

Avoid using `global` unless absolutely necessary.

Good:

```python
def update_customer(customer):
    return "Mary Johnson"
```

Better design than modifying global state.