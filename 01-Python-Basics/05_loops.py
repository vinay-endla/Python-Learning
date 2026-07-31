customers = [
    "John Smith",
    "Mary Johnson",
    "David Lee",
    "Sarah Brown"
]

monthly_usage = [
    842,
    1200,
    430,
    1800
]

solar_customers = [
    True,
    False,
    True,
    False
]

FIXED_CHARGE = 25
FIXED_SOLAR_REBATE = 10

LOW_USAGE_RATE = 0.12
STANDARD_USAGE_RATE = 0.15
HIGH_USAGE_RATE = 0.18

ENVIRONMENTAL_SURCHARGE = 35


for customer_index, (customer, usage, solar_customer) in enumerate(
    zip(customers, monthly_usage, solar_customers),
    start=1
):

    # Determine rate
    if usage <= 500:
        rate_per_kwh = LOW_USAGE_RATE
    elif usage <= 1000:
        rate_per_kwh = STANDARD_USAGE_RATE
    else:
        rate_per_kwh = HIGH_USAGE_RATE

    # Calculate base bill
    energy_charge = usage * rate_per_kwh
    environmental_surcharge = 0
    solar_credit = 0

    # Apply independent billing rules
    if usage > 1500:
        environmental_surcharge = ENVIRONMENTAL_SURCHARGE

    if solar_customer:
        solar_credit = FIXED_SOLAR_REBATE

    # Calculate final bill
    total_bill = (
        energy_charge
        + FIXED_CHARGE
        + environmental_surcharge
        - solar_credit
    )

    # Print bill
    print("=" * 45)
    print(f"UTILITY BILL FOR CUSTOMER {customer_index}: {customer}")
    print("=" * 45)
    print(f"Customer                  : {customer}")
    print(f"Usage                     : {usage} kWh")
    print(f"Rate                      : ${rate_per_kwh:.2f}/kWh")
    print(f"Energy Charge             : ${energy_charge:.2f}")
    print(f"Fixed Charge              : ${FIXED_CHARGE:.2f}")
    print(f"Environmental Surcharge   : ${environmental_surcharge:.2f}")
    print(f"Solar Credit              : -${solar_credit:.2f}")
    print("-" * 45)
    print(f"Total Bill                : ${total_bill:.2f}")
    print("=" * 45)