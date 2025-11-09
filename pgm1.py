#Write a program to check whether a number is prime or not.
def isPrime(a):
    if a <= 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

b = int(input("Enter a number: "))
if isPrime(b):
    print(f"The number {b} is a Prime number!")
else:
    print(f"The number {b} is not a Prime number!")
