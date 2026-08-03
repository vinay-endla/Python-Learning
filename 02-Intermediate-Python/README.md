# 02 - Intermediate Python

This module focuses on writing Python the way professional software projects are organized.

---

# Lessons Completed

## 01. Modules & Imports

Topics Covered:

- What is a module
- Why modules exist
- Organizing code into multiple files
- Creating custom modules
- Importing modules
- Importing specific functions
- Importing multiple functions
- Module aliases
- Function aliases
- Calling functions from other modules
- Multi-file Python applications

Project Structure:

```
02-Intermediate-Python/
│
├── billing.py
├── customers.py
├── main.py
├── Notes.md
└── README.md
```

Import Styles Learned:

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

Files:

- billing.py
- customers.py
- main.py

---

# Upcoming Lessons

- Variable Scope
- Tuples (Deep Dive)
- Sets
- Exception Handling
- List Comprehensions
- File Handling
- Packages
- Virtual Environments