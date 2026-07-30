# Customer Information

customer_name = "John Smith"
meter_id = "MTR100245"
city = "Philadelphia"
monthly_usage = 842
bill_amount = 126.35
solar_customer = True

print("=" * 40)
print("UTILITY CUSTOMER REPORT")
print("=" * 40)
print()
print(f"Customer Name : {customer_name}")
print()
print(f"Meter ID      : {meter_id}")
print()
print(f"City          : {city}")
print()
print(f"Monthly Usage : {monthly_usage} kWh")
print()
print(f"Bill Amount   : ${bill_amount:.2f}")
print()
print(f"Solar         : {solar_customer}")
print()
print("=" * 40)

