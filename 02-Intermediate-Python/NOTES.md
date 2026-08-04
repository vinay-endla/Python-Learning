# Module 2 Notes

---

# 1. Modules and Imports

## What Is a Module?

A module is a Python file containing reusable code.

Examples:

```text
billing.py
customers.py
main.py
```

Modules allow an application to be divided by responsibility.

---

## Import an Entire Module

```python
import billing

billing.calculate_bill()
billing.print_invoice()
```

This style makes the function's source clear.

---

## Module Alias

```python
import billing as bill

bill.calculate_bill()
```

Common library aliases include:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

---

## Import a Specific Function

```python
from billing import calculate_bill

calculate_bill()
```

This is useful when only a small number of functions are needed.

---

## Import Multiple Functions

```python
from billing import (
    calculate_bill,
    print_invoice,
    say_hello,
)
```

Parentheses make long imports easier to read.

---

## Function Aliases

```python
from billing import (
    calculate_bill as calc_bill,
    print_invoice as invoice,
)
```

Aliases can:

- Shorten long names
- Resolve naming conflicts
- Improve readability

---

## Avoid Wildcard Imports

Avoid:

```python
from billing import *
```

Problems:

- The source of names becomes unclear.
- Naming conflicts can occur.
- Code becomes harder to review and maintain.

---

## Common Error

```text
NameError: name 'billing' is not defined
```

Cause:

```python
billing.calculate_bill()
```

was used before importing `billing`.

Correct:

```python
import billing
```

---

# 2. Variable Scope

## Global Scope

A variable created outside a function is global to that module.

```python
customer = "John Smith"
```

A function can normally read it:

```python
def print_customer():
    print(customer)
```

---

## Local Scope

A variable created inside a function is local to that function.

```python
def update_customer():
    customer = "Mary Johnson"
```

The local variable exists only during that function call.

---

## Variable Shadowing

A local variable can have the same name as a global variable.

```python
customer = "John Smith"

def update_customer():
    customer = "Mary Johnson"
```

Inside the function:

```text
customer = Mary Johnson
```

Outside the function:

```text
customer = John Smith
```

The local variable temporarily hides the global variable.

---

## Each Function Has Its Own Local Scope

One function cannot directly access another function's local variables.

Bad dependency:

```python
def print_customer():
    print(customer)
```

Better:

```python
def print_customer(customer):
    print(customer)
```

Pass the required value through a parameter.

---

## Parameters Are Local Variables

```python
def print_customer(customer):
    print(customer)
```

The parameter `customer` exists locally inside the function.

---

## The `global` Keyword

```python
customer = "John Smith"

def update_customer():
    global customer
    customer = "Mary Johnson"
```

`global customer` tells Python to modify the global variable instead of creating a local variable.

Use this sparingly.

---

## Professional Recommendation

Prefer:

```python
def update_customer(customer):
    return "Mary Johnson"
```

over modifying shared global state.

Explicit inputs and return values make code easier to:

- Test
- Understand
- Reuse
- Debug

---

# 3. Tuples

## What Is a Tuple?

A tuple is an ordered, immutable collection.

```python
customer = (
    "John Smith",
    "MTR-001",
    842,
    True,
)
```

---

## Indexing

```python
customer[0]
customer[1]
```

Negative indexes count from the end:

```python
customer[-1]
customer[-2]
```

`-1` means the last item.

---

## Tuple Length

```python
len(customer)
```

Returns the number of items.

---

## Immutability

Tuple items cannot be replaced.

Invalid:

```python
customer[0] = "Mary Johnson"
```

Error:

```text
TypeError: 'tuple' object does not support item assignment
```

Tuples also do not support list methods such as:

```python
append()
remove()
```

---

## Basic Unpacking

```python
name, meter_number, usage, is_solar = customer
```

The number of variables must match the number of tuple values.

---

## Unpacking Error

```python
name, meter_number = customer
```

Error:

```text
ValueError: too many values to unpack
```

Python had more values than available variables.

---

## Extended Unpacking

### Capture Everything After the First Value

```python
first, *rest = customer
```

`rest` becomes a list.

### Capture Everything Before the Last Value

```python
*rest, last = customer
```

### Capture the Middle

```python
first, *middle, last = customer
```

The starred variable always receives a list.

---

## Nested Unpacking

```python
customer = (
    "John Smith",
    ("MTR-001", 842),
    True,
)

name, (meter_number, usage), is_solar = customer
```

The nested tuple is unpacked into separate variables.

---

## Variable Swapping

```python
a = 10
b = 20

a, b = b, a
```

Python evaluates the right side first and then unpacks the values:

```text
a = 20
b = 10
```

---

## Tuple Unpacking in Loops

### `zip()`

```python
for customer, usage, is_solar in zip(
    customers,
    usages,
    solar_customers,
):
    ...
```

### `enumerate()`

```python
for index, customer in enumerate(customers, start=1):
    ...
```

### `dict.items()`

```python
for key, value in customer.items():
    ...
```

These operations produce grouped values that Python unpacks.

---

# 4. Sets

## What Is a Set?

A set is an unordered, mutable collection of unique values.

```python
customers = {
    "John",
    "Mary",
    "David",
}
```

---

## Set Properties

- Unordered
- Mutable
- No indexes
- Duplicate values are ignored
- Useful for membership testing
- Useful for comparing collections

---

## Empty Set

This creates an empty dictionary:

```python
empty = {}
```

This creates an empty set:

```python
empty = set()
```

---

## Removing Duplicates

```python
meters = [
    "MTR-001",
    "MTR-002",
    "MTR-001",
]

unique_meters = set(meters)
```

Result contains only unique meter numbers.

---

## Add an Element

```python
customers.add("Sarah")
```

Adding an existing value has no effect.

---

## Remove an Element

```python
customers.remove("Mary")
```

If the value is missing:

```text
KeyError
```

---

## Safely Remove an Element

```python
customers.discard("Vinay")
```

If the value does not exist, nothing happens.

---

## Membership Testing

```python
"John" in customers
```

Returns:

```python
True
```

or:

```python
False
```

---

## Clear a Set

```python
customers.clear()
```

The empty set prints as:

```text
set()
```

---

## Set Operations

Assume:

```python
A = {"John", "Mary", "David"}
B = {"Mary", "David", "Sarah"}
```

### Union

```python
A | B
```

Mathematics:

```text
A ∪ B
```

Meaning: all values from both sets.

---

### Intersection

```python
A & B
```

Mathematics:

```text
A ∩ B
```

Meaning: values common to both sets.

---

### Difference

```python
A - B
```

Meaning: values in `A` but not in `B`.

Difference is directional:

```text
A - B is not necessarily equal to B - A
```

---

### Symmetric Difference

```python
A ^ B
```

Equivalent to:

```text
(A - B) ∪ (B - A)
```

Meaning: values that belong to exactly one set.

---

## Professional Set Uses

- Removing duplicate customer IDs
- Comparing meter datasets
- Finding missing records
- Finding common records
- Permission checks
- Data-cleaning workflows
- AI and analytics preprocessing

---

# 5. Exception Handling

## What Is an Exception?

An exception is an error that occurs while a program is running.

Examples:

```text
NameError
KeyError
TypeError
ValueError
ZeroDivisionError
FileNotFoundError
```

Without a matching handler, an exception terminates the program.

---

## Basic `try` and `except`

```python
try:
    print(10 / 0)

except:
    print("An error occurred.")
```

The `try` block contains risky code.

The `except` block handles an exception.

---

## Execution Rule

When an exception occurs inside `try`:

1. The remaining lines in the `try` block are skipped.
2. Python searches for a matching `except` block.
3. The matching handler executes.
4. Execution continues after the exception-handling structure.

Example:

```python
try:
    print("A")
    print(10 / 0)
    print("B")

except ZeroDivisionError:
    print("C")

print("D")
```

Output:

```text
A
C
D
```

`B` never executes.

---

## Catch Specific Exceptions

Prefer:

```python
try:
    result = 100 / number

except ZeroDivisionError:
    print("Number cannot be zero.")
```

over:

```python
except:
    print("An error occurred.")
```

Specific handlers prevent unrelated problems from being misidentified.

---

## Multiple Exception Handlers

```python
try:
    number = int(input("Enter a number: "))
    print(100 / number)
    print(customer["phone"])

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")

except KeyError:
    print("Phone number not found.")
```

Only the first matching handler executes.

---

## Exception Matching Order

Python checks exception handlers from top to bottom.

Specific handlers should come first.

Correct:

```python
except ZeroDivisionError:
    ...

except Exception:
    ...
```

Poor ordering:

```python
except Exception:
    ...

except ZeroDivisionError:
    ...
```

The general handler would catch the exception before the specific handler could.

---

## Exception Hierarchy

`Exception` is a broad parent type.

Examples derived from it include:

```text
ValueError
KeyError
TypeError
ZeroDivisionError
FileNotFoundError
```

A broad handler can catch many exception types:

```python
except Exception:
    print("Unexpected error.")
```

Use it last.

---

## `else`

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print(result)
```

`else` runs only if the entire `try` block completes without an exception.

Use it for logic that depends on successful execution.

---

## `finally`

```python
try:
    process_data()

finally:
    close_resources()
```

`finally` runs whether:

- The operation succeeds
- A handled exception occurs
- An unhandled exception occurs
- A function returns early
- The current block exits

---

## Why `finally` Is Different from Code After `try`

Code placed after exception handling runs only if execution reaches it.

An unhandled exception may prevent that.

`finally` is guaranteed to run before Python leaves the block.

Use it for cleanup such as:

- Closing files
- Closing database connections
- Releasing locks
- Closing sockets
- Removing temporary resources

---

## Complete Structure

```python
try:
    # Risky operation

except ValueError:
    # Handle invalid values

except ZeroDivisionError:
    # Handle division by zero

except Exception:
    # Handle unexpected failures

else:
    # Run after successful try block

finally:
    # Always perform cleanup
```

---

## Professional Exception-Handling Rules

- Catch exceptions you can meaningfully handle.
- Prefer specific exception types.
- Put general handlers last.
- Do not silently hide errors.
- Keep risky `try` blocks reasonably focused.
- Use `else` for success-dependent logic.
- Use `finally` for guaranteed cleanup.
- Provide useful messages rather than vague output.