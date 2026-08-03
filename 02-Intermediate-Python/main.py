
import billing as bill 

bill.calculate_bill("John Doe", 100)
bill.say_hello()
bill.print_invoice("John Doe", 150.00)


from billing import (calculate_bill as calc_bill, say_hello as hello, print_invoice as invoice)


calc_bill("John Doe", 100)
hello()
invoice("John Doe", 150.00)

