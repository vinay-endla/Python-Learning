from billing import calculate_bill as calc_bill

calc_bill("John Doe", 100)

from billing import (
    calculate_bill as calc_bill,
    print_invoice as invoice,
    say_hello as hello,
)

calc_bill("John Doe", 100)
hello()
invoice("John Doe", 150)