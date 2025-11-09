"""
A program that accepts 2 strings & returns the indices of all the occurances of the 2nd string in the 1st string as a list.
If the 2nd is not present in the 1st string, then it should return -1.
"""
def findSubString(main, sub):
    indices = []
    start = 0

    while True:
        index = main.find(sub, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1
    if indices:
        return indices
    else:
        return "Nothing in this shit!"

main = str(input("Enter the main string: "))
sub = str(input("Enter the substring to search for: "))
result = findSubString(main, sub)
print("Result: ", result)
