""""
Write a program to handle a ZeroDivisionError exception when dividing a number by Zero.
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    print("Result: ", numerator / denominator)

except ZeroDivisionError:
    print("Error: Cannot divide by Zero!")
