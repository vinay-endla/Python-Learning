def print_line():
    print("=" * 45)


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


def determine_rate(usage):
    if usage <= 500:
        return LOW_USAGE_RATE
    elif usage <= 1000:
        return STANDARD_USAGE_RATE
    else:
        return HIGH_USAGE_RATE


def calculate_energy_charge(usage):
    return usage * determine_rate(usage)


def calculate_environmental_surcharge(usage):
    if usage > 2000:
        return ENVIRONMENTAL_SURCHARGE
    else:
        return 0


def calculate_solar_credit(is_solar):
    if is_solar:
        return FIXED_SOLAR_REBATE
    else:
        return 0


def calculate_total_bill(
    energy_charge,
    environmental_surcharge,
    solar_credit
):
    return (
        energy_charge
        + FIXED_CHARGE
        + environmental_surcharge
        - solar_credit
    )


def print_customer_info(customer_index, customer, usage, is_solar):
    rate_per_kwh = determine_rate(usage)
    energy_charge = calculate_energy_charge(usage)

    environmental_surcharge = calculate_environmental_surcharge(
        usage
    )

    solar_credit = calculate_solar_credit(is_solar)

    total_bill = calculate_total_bill(
        energy_charge,
        environmental_surcharge,
        solar_credit
    )

    print_line()
    print(f"{f'Customer {customer_index}':^45}")
    print_line()
    print(f"Customer                  : {customer}")
    print(f"Usage                     : {usage} kWh")
    print(f"Rate                      : ${rate_per_kwh:.2f}/kWh")
    print(f"Energy Charge             : ${energy_charge:.2f}")
    print(f"Fixed Charge              : ${FIXED_CHARGE:.2f}")
    print(f"Environmental Surcharge   : ${environmental_surcharge:.2f}")
    print(f"Solar Credit              : -${solar_credit:.2f}")
    print(f"Total Bill                : ${total_bill:.2f}")

    if is_solar:
        print("Solar Customer            : Yes")
    else:
        print("Solar Customer            : No")

    print_line()
    print()

for customer_index, (customer, usage, is_solar) in enumerate(
    zip(customers, monthly_usage, solar_customers),
    start=1
):
    print_customer_info(
        customer_index,
        customer,
        usage,
        is_solar
    )