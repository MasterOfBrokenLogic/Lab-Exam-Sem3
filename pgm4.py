#Program to print the summation of the following series upto n, "1 - 2 + 3 - 4 + .........n"
def sum(n):
    totalSum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            totalSum += i
    return totalSum

num= int(input("Enter the number of terms(n): "))

result = sum(num)

print("The summation of the series upto {num} terms is: ", result)
