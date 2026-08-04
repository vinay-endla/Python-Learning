# 02 - Intermediate Python

This module focuses on writing Python in a more structured, reusable, and professional way.

The lessons build on Python fundamentals and introduce concepts used in larger applications, data processing, enterprise software, and future AI projects.

---

# Lessons Completed

## 01. Modules and Imports

### Topics Covered

- What a Python module is
- Why applications use multiple files
- Creating custom modules
- Importing an entire module
- Importing specific functions
- Importing multiple functions
- Module aliases
- Function aliases
- Calling functions across files
- Avoiding wildcard imports

### Import Styles

```python
import billing
```

```python
import billing as bill
```

```python
from billing import calculate_bill
```

```python
from billing import (
    calculate_bill,
    print_invoice,
)
```

```python
from billing import (
    calculate_bill as calc_bill,
    print_invoice as invoice,
)
```

### Files

- `billing.py`
- `customers.py`
- `main.py`

---

## 02. Variable Scope

### Topics Covered

- Global scope
- Local scope
- Function scope
- Parameter scope
- Variable shadowing
- Separate local scopes for different functions
- Reading global variables from functions
- The `global` keyword
- Passing data through parameters
- Avoiding unnecessary global state

### Key Principle

Functions should normally receive the data they need through parameters instead of depending on global variables.

### File

- `02_scope.py`

---

## 03. Tuples

### Topics Covered

- Creating tuples
- Tuple indexing
- Negative indexing
- Tuple length
- Tuple immutability
- Basic tuple unpacking
- Extended unpacking using `*`
- Nested unpacking
- Tuple packing
- Variable swapping
- Unpacking values from `zip()`
- Unpacking values from `enumerate()`
- Unpacking key-value pairs from `dict.items()`

### Key Principle

Tuples are ordered collections that cannot be modified after creation.

### File

- `03_tuples.py`

---

## 04. Sets

### Topics Covered

- Creating sets
- Creating an empty set
- Converting lists and tuples into sets
- Removing duplicate values
- Unordered collections
- Unique values
- Membership testing with `in`
- Adding values with `add()`
- Removing values with `remove()`
- Safe removal with `discard()`
- Clearing sets with `clear()`
- Iterating through sets
- Union
- Intersection
- Difference
- Symmetric difference

### Set Operators

```python
A | B
```

Union: everything from both sets.

```python
A & B
```

Intersection: values common to both sets.

```python
A - B
```

Difference: values in `A` but not in `B`.

```python
A ^ B
```

Symmetric difference: values found in exactly one set.

### File

- `04_sets.py`

---

## 05. Exception Handling

### Topics Covered

- Runtime exceptions
- Program termination after an unhandled exception
- `try`
- `except`
- Catching specific exceptions
- Multiple `except` blocks
- Exception matching
- Exception hierarchy
- General `Exception` handlers
- Correct exception-handler ordering
- `else`
- `finally`
- Cleanup logic
- Continuing execution after handled exceptions

### Exceptions Practiced

- `NameError`
- `KeyError`
- `TypeError`
- `ValueError`
- `ZeroDivisionError`
- `FileNotFoundError`

### Complete Structure

```python
try:
    # Risky code

except ValueError:
    # Handle invalid values

except ZeroDivisionError:
    # Handle division by zero

except Exception:
    # Handle unexpected exceptions

else:
    # Run only if the try block succeeds

finally:
    # Run no matter what
```

### Key Principles

- Catch specific exceptions whenever possible.
- Put specific exception handlers before general handlers.
- The first matching `except` block handles the exception.
- An exception immediately stops the remaining code in the `try` block.
- `else` runs only when the entire `try` block succeeds.
- `finally` runs whether the operation succeeds or fails.
- Use `finally` for cleanup that must happen even after an uncaught exception or early exit.

### File

- `05_exception_handling.py`

---

# Intermediate Python Progress

- ✅ Modules and Imports
- ✅ Variable Scope
- ✅ Tuples
- ✅ Sets
- ✅ Exception Handling
- ⏳ List Comprehensions
- ⏳ File Handling
- ⏳ Packages
- ⏳ Virtual Environments

---

## 06. List Comprehensions

### Topics Covered

- Why list comprehensions exist
- Transforming every element
- Filtering elements
- Conditional transformations
- Reading comprehensions in plain English
- Comparing loops with comprehensions
- Writing clean, readable comprehensions

### Patterns Learned

#### Transform

```python
[
    expression
    for variable in iterable
]
```

#### Filter

```python
[
    expression
    for variable in iterable
    if condition
]
```

#### Conditional Transform

```python
[
    expression_if_true if condition else expression_if_false
    for variable in iterable
]
```

### Key Principles

- List comprehensions replace common loop + append patterns.
- They do not introduce a new looping algorithm.
- Read them as:
  - "For each item in collection, produce ..."
- Use a trailing `if` to **filter** items.
- Use `if...else` inside the expression to **transform** every item.

### File

- `06_list_comprehensions.py`

# Intermediate Python Progress

- ✅ Modules and Imports
- ✅ Variable Scope
- ✅ Tuples
- ✅ Sets
- ✅ Exception Handling
- ✅ List Comprehensions
- ⏳ File Handling
- ⏳ Packages
- ⏳ Virtual Environments