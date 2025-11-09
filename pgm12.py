"""
Write a progam that reads a list of integers from the user and throws and exception if any numbers are duplicates.
"""
def checkDuplicate(list):
    if len(list) != len(set(list)):
        raise Exception("Duplicate values found!")
    else:
        print("No duplicates found!")

nums = list(map(int, input("Enter the numbers separated by space: ").split()))

try:
    checkDuplicate(nums)
except Exception as e:
    print(e)
