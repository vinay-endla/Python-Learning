# Python Learning Notes

Author: Vinay Kumar Endla

---

# Module 1 - Variables

## Concepts Learned

- Variables store data in memory.
- Variable names should clearly describe their purpose.
- Python variables do not require explicit data types.

Example:

```python
customer_name = "John Smith"
monthly_usage = 842
```

## Best Practices

- Use meaningful variable names.
- Follow snake_case naming convention.
- Avoid abbreviations unless they are industry standard.

Good:

```python
monthly_usage
energy_charge
customer_name
```

Bad:

```python
x
a
temp1
```

## Utility Industry Example

Variables represent business information such as:

- Customer Name
- Meter ID
- Monthly Usage
- Bill Amount

---

# Module 2 - Data Types

## Concepts Learned

Python automatically determines data types.

### String (str)

Stores text.

```python
customer_name = "John Smith"
```

### Integer (int)

Whole numbers.

```python
monthly_usage = 842
```

### Float (float)

Decimal numbers.

```python
bill_amount = 126.35
```

### Boolean (bool)

True or False.

```python
solar_customer = True
```

## Useful Function

```python
type(variable)
```

Returns the data type.

## Utility Industry Example

| Data | Python Type |
|-------|-------------|
| Customer Name | String |
| Monthly Usage | Integer |
| Bill Amount | Float |
| Solar Customer | Boolean |

---

# Module 3 - Operators

## Concepts Learned

### Arithmetic Operators

```python
+
-
*
/
```

### Assignment Operator

```python
=
```

### Compound Assignment

```python
+=
-=
*=
/=
```

## Example

```python
energy_charge = monthly_usage * rate_per_kwh

total_bill = energy_charge + FIXED_CHARGE
```

## Constants

Values that should not change during program execution.

Example:

```python
FIXED_CHARGE = 25
LOW_USAGE_RATE = 0.12
```

Convention:

Constants use uppercase names.

## Utility Industry Example

Calculate:

- Energy Charge
- Fixed Charge
- Total Bill

---

# Module 4 - Conditional Statements

## Concepts Learned

Programs can make decisions.

Python provides:

```python
if

elif

else
```

Example:

```python
if solar_customer:
    total_bill -= FIXED_SOLAR_REBATE
```

## Comparison Operators

```python
>
<
>=
<=
==
!=
```

## Business Rules

Business rules determine how bills are calculated.

Examples:

- Solar rebate
- High usage surcharge
- Pricing tiers

## Pricing Slabs

```python
if monthly_usage <= 500:
    rate_per_kwh = LOW_USAGE_RATE

elif monthly_usage <= 1000:
    rate_per_kwh = STANDARD_USAGE_RATE

else:
    rate_per_kwh = HIGH_USAGE_RATE
```

## Engineering Lesson

Always separate the program into logical phases.

```
Input

↓

Determine Business Rules

↓

Perform Calculations

↓

Generate Output
```

Do **not** mix calculations inside the print statements.

Bad:

```python
print(...)
total_bill += surcharge
```

Good:

```python
Determine all values

↓

Calculate final bill

↓

Print report
```

## Utility Industry Example

Business rules may include:

- Solar rebate
- Environmental surcharge
- Time-of-use pricing
- Peak demand charges
- Senior citizen discounts
- Electric vehicle incentives

---

# Key Python Style Guidelines Learned

- Use descriptive variable names.
- Use constants for fixed values.
- Keep calculations separate from presentation.
- Follow consistent formatting.
- Write readable code before writing clever code.

---

# Git Commands

Check repository status

```bash
git status
```

Stage all changes

```bash
git add .
```

Create a commit

```bash
git commit -m "Meaningful commit message"
```

Upload to GitHub

```bash
git push
```

---

# Engineering Lessons Learned

Software development is more than writing code.

A professional workflow is:

```
Understand the problem

↓

Design the solution

↓

Write code

↓

Run the program

↓

Test

↓

Review

↓

Commit

↓

Push to GitHub
```

Always prioritize:

- Readability
- Maintainability
- Correctness

before optimization.