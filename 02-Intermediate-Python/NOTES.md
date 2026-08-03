# Module 2 Notes

---

# Modules

A module is simply a Python (.py) file.

Modules allow us to organize code into reusable, maintainable components.

Instead of one huge file, applications are divided into multiple modules based on responsibility.

Example:

```
billing.py
customers.py
reports.py
payments.py
main.py
```

---

# Why Modules?

Modules help:

- Organize code
- Improve readability
- Encourage code reuse
- Simplify maintenance
- Separate responsibilities

Functions organize a large function.

Modules organize a large application.

---

# Import Entire Module

```python
import billing

billing.calculate_bill()
billing.say_hello()
```

Advantages:

- Clear where functions come from.
- Preferred when using many functions from the same module.

---

# Module Alias

```python
import billing as bill

bill.calculate_bill()
```

Useful when module names are long.

Industry examples:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

---

# Import Specific Functions

```python
from billing import calculate_bill

calculate_bill()
```

Advantages:

- Less typing.
- Good when only a few functions are needed.

---

# Import Multiple Functions

```python
from billing import (
    calculate_bill,
    say_hello,
    print_invoice,
)
```

Preferred formatting when importing several functions.

---

# Function Aliases

```python
from billing import (
    calculate_bill as calc_bill,
    print_invoice as invoice,
)
```

Useful for:

- Shorter names
- Avoiding naming conflicts

---

# Avoid

```python
from billing import *
```

Reason:

- Imports everything.
- Makes code harder to understand.
- Can create naming conflicts.

---

# Common Error

```
NameError:
name 'billing' is not defined
```

Cause:

Attempting to use a module before importing it.

Example:

```python
billing.calculate_bill()
```

Correct:

```python
import billing

billing.calculate_bill()
```

---

# Professional Recommendation

For your own project modules:

```python
import billing
import customers
import reports
```

Then:

```python
billing.calculate_bill()
customers.find_customer()
reports.generate_report()
```

This clearly shows which module owns each function.