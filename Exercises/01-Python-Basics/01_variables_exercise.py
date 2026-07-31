# Exercise 1: Variables
customer_name = "John Smith"
meter_number = "MTR-001"
monthly_usage = 842
is_solar_customer = True

print(f"{'Exercise 1: Variables':=^45}")
print(f"Customer Name        : {customer_name}")
print(f"Meter Number         : {meter_number}")
print(f"Monthly Usage        : {monthly_usage} kWh")
print(f"Solar Customer       : {'Yes' if is_solar_customer else 'No'}")


# Exercise 2: Constants
FIXED_CHARGE = 25.00
LOW_USAGE_RATE = 0.10
print(f"{'Exercise 2: Constants':=^45}")
print(f"Fixed Charge         : ${FIXED_CHARGE:.2f}")
print(f"Low Usage Rate       : ${LOW_USAGE_RATE:.2f}")
print(f"Energy Charge        : ${monthly_usage * LOW_USAGE_RATE:.2f}")


# Exercise 3: Arithmetic
prev_reading = 1200
curr_reading = 2042
usage = curr_reading - prev_reading
print(f"{'Exercise 3: Arithmetic':=^45}")
print(f"Previous Reading     : {prev_reading} kWh")
print(f"Current Reading      : {curr_reading} kWh")
print(f"Usage                : {usage} kWh")


# Exercise 4: Customer Information
customer_city = "Philadelphia"
customer_state = "PA"
customer_zip_code = "19103"

print(f"{'Exercise 4: Customer Information':=^45}")
print(f"Name    : {customer_name}")
print(f"City    : {customer_city}")
print(f"State   : {customer_state}")
print(f"ZIP     : {customer_zip_code}")


# Exercise 5: Total Bill
energy_charge = monthly_usage * LOW_USAGE_RATE
solar_credit = 10.00
total_bill = energy_charge + FIXED_CHARGE - solar_credit

print(f"{'Exercise 5: Total Bill':=^45}")
print(f"Energy Charge : ${energy_charge:.2f}")
print(f"Fixed Charge  : ${FIXED_CHARGE:.2f}")
print(f"Solar Credit  : -${solar_credit:.2f}")
print("--------------------------------")
print(f"Total Bill    : ${total_bill:.2f}")


# Exercise 6: Bill Header
utility_name = "PECO ELECTRIC COMPANY"
billing_month = "July 2026"
bill_usage = 842

print(f"{'Exercise 6: Bill Header':=^45}")
print("=" * 45)
print(f"{utility_name:^45}")
print("=" * 45)
print(f"Customer : {customer_name}")
print(f"Month    : {billing_month}")
print(f"Usage    : {bill_usage} kWh")
print("=" * 45)


# Exercise 7: Customer Summary
customer_id = "CUS-1001"
service_address = "123 Market Street"
summary_meter_number = "MTR-001"
summary_monthly_usage = 842
summary_solar_customer = True
summary_bill_amount = 141.30

print(f"{'Exercise 7: Customer Summary':=^45}")
print(f"Customer ID       : {customer_id}")
print(f"Customer Name     : {customer_name}")
print(f"Service Address   : {service_address}")
print(f"Meter Number      : {summary_meter_number}")
print(f"Monthly Usage     : {summary_monthly_usage} kWh")
print(
    f"Solar Customer    : "
    f"{'Yes' if summary_solar_customer else 'No'}"
)
print(f"Bill Amount       : ${summary_bill_amount:.2f}")


# Exercise 8: Meaningful variable names
# Meaningful names make code easier to read and understand.
# They help developers quickly identify what each value represents.
# Clear names reduce mistakes when code is changed or extended.
# They make collaboration easier because the intent is visible.
# They also make debugging and reviewing enterprise code faster.


# Exercise 9: Professional Variable Names
professional_customer_name = "John"
monthly_energy_usage = 842
is_solar_customer = True
energy_charge_amount = 126.30


# Exercise 10: Utility Billing Input Template

# Customer information
template_customer_id = "CUS-1001"
template_service_address = "123 Market Street"
template_city = "Philadelphia"
template_state = "PA"
template_zip_code = "19103"

# Meter and billing information
template_meter_number = "MTR-001"
template_billing_month = "July 2026"
template_previous_reading = 1200
template_current_reading = 2042
template_monthly_usage = 842
template_solar_customer = True

# Billing amounts
template_energy_charge = 126.30
template_fixed_charge = 25.00
template_solar_credit = 10.00

# Billing constants
STANDARD_FIXED_CHARGE = 25.00
STANDARD_ENERGY_RATE = 0.15
SOLAR_CREDIT_RATE = 0.02
LATE_PAYMENT_FEE = 15.00
TAX_RATE = 0.08
