#Program to check whether a number is Odd or Even.
def oddEven(n):
    if n % 2 == 0:
        return True

num = int(input("Enter the number: "))

if oddEven(num):
    print(f"The number {num} is Even!")
else:
    print(f"The number {num} is Odd!")
