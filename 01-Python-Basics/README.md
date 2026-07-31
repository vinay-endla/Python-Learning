# Python Basics

This folder contains my foundational Python learning journey.

The focus is not only on learning Python syntax but also on developing software engineering principles through practical, enterprise-style examples inspired by the utility industry.

---

# Modules Completed

## ✅ Module 1 - Variables

### Topics Covered

- Variables
- Naming conventions
- Constants
- Python naming style (snake_case)

### Key Concepts

- Store information using variables
- Use meaningful names
- Separate constants from changing values

---

## ✅ Module 2 - Data Types

### Topics Covered

- String
- Integer
- Float
- Boolean

### Key Concepts

- Python is dynamically typed
- Understanding appropriate data types for business information

---

## ✅ Module 3 - Operators

### Topics Covered

- Arithmetic operators
- Assignment operators
- Compound assignment

### Key Concepts

- Mathematical calculations
- Updating values
- Utility bill calculations

---

## ✅ Module 4 - Conditional Statements

### Topics Covered

- if
- elif
- else
- Comparison operators

### Key Concepts

Business rules drive software behavior.

Examples include:

- Pricing tiers
- Solar rebates
- Environmental surcharges

---

## ✅ Module 5 - Loops

### Topics Covered

- Lists
- for loops
- zip()
- enumerate()

### Key Concepts

Process multiple customers using a single block of code.

Learned how to iterate over multiple related collections simultaneously.

Example:

```python
for customer, usage, is_solar in zip(...):
```

Using enumerate:

```python
for customer_index, (...) in enumerate(..., start=1):
```

---

## ✅ Module 6 - Functions

### Topics Covered

- Function definition
- Parameters
- Function calls
- Reusable code

### Key Concepts

Break programs into small reusable units.

Example:

```python
def print_customer_info(...):
```

Each function should have one clear responsibility.

---

## ✅ Module 7 - Return Values

### Topics Covered

- return
- Returning multiple values
- Function composition

### Key Concepts

Functions should calculate and return data rather than only printing.

Example:

```python
rate = determine_rate(usage)

energy_charge = calculate_energy_charge(usage)

total_bill = calculate_total_bill(...)
```

Functions now work together like building blocks.

---

# Mini Utility Billing System

Built a console-based billing system featuring:

- Tiered electricity pricing
- Fixed customer charges
- Solar customer credits
- Environmental surcharge
- Multiple customer processing
- Formatted bill generation

Implemented using:

- Variables
- Lists
- Loops
- Functions
- Return values
- zip()
- enumerate()

---

# Software Engineering Principles Learned

- Write readable code.
- One function should perform one responsibility.
- Separate business logic from presentation.
- Avoid duplicated code (DRY Principle).
- Build reusable functions.
- Use meaningful variable and function names.
- Organize programs into logical steps.
- Calculate values once and reuse them.
- Functions should return values whenever appropriate.

---

# Current Repository Structure

```
01-Python-Basics
│
├── 01_variables.py
├── 02_data_types.py
├── 03_operators.py
├── 04_conditions.py
├── 05_loops.py
├── 06_functions.py
├── Notes.md
└── README.md
```

---

# Skills Acquired

- Python fundamentals
- Basic problem decomposition
- Business rule implementation
- Function design
- Loop processing
- Code organization
- Git workflow
- VS Code development workflow

---

# Next Learning Modules

- Dictionaries
- Tuples
- Classes & Objects
- File Handling
- Exception Handling
- Modules & Packages
- Object-Oriented Programming
- Data Processing
- Testing