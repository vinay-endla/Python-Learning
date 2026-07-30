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

label_width = 15
print(f"{'Customer Name'.ljust(label_width)}: {customer_name}")
print(f"{'Meter ID'.ljust(label_width)}: {meter_id}")
print(f"{'City'.ljust(label_width)}: {city}")
print(f"{'Monthly Usage'.ljust(label_width)}: {monthly_usage} kWh")
print(f"{'Bill Amount'.ljust(label_width)}: ${bill_amount:.2f}")
print(f"{'Solar'.ljust(label_width)}: {solar_customer}")
print()
print("=" * 40)

