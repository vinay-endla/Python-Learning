# number = 10

# print(number)

# try:
#     print(10 / 0)
# except:
#     print("An error occurred.")

# print("Program Finished")

# try:
#     print("A")
#     print(10 / 0)
#     print("B")
#     print("C")
# except:
#     print("D")

# print("E")

# try:
#     print("A")
#     print(10 / 2)
#     print("B")
# except:
#     print("C")

# print("D")

# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# customer = {
#     "name": "John Smith"
# }

# try:
#     print(10 / 0)
#     print(customer["phone"])

# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except KeyError:
#     print("Phone number not found.")

# print("Program Finished")

customer = {
    "name": "John Smith"
}

try:
    number = int(input("Enter a number: "))
    print(100 / number)
    # print(customer["phone"])


except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")

except Exception:
    print("General error")

except KeyError:
    print("Phone number not found.")

else:
    print("Everything executed successfully.")

finally:
    print("Cleaning up resources.")
    
print("Program Finished")