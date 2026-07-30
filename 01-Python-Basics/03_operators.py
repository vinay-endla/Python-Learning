customer_name = "John Smith"
monthly_usage = 842
solar_customer = True

RATE_PER_KWH = 0.15345
FIXED_CHARGE = 25

energy_charge = monthly_usage * RATE_PER_KWH
total_charge = energy_charge + FIXED_CHARGE

print(f"{'='*40}")
print(f"Customer: {customer_name}")
print(f"Monthly Usage    : {monthly_usage} kWh")
print(f"Energy Charge    : ${energy_charge:.2f}")
print(f"Fixed Charge     : ${FIXED_CHARGE:.2f}")
print(f"Total Charge     : ${total_charge:.2f}")
