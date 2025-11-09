"""
Consider a tuple t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10).
Write a program to find the following operations:
  a) Print the contents of 't1' in 2 seperate lines, such that half of the values appear on the 1st line and the other half on the 2nd line. 
  b) Print all the even values of 't1' as another tuple 't2'
  c) Concatenate a tuple t2 = (11, 13, 15) with 't1'
  d) Return the max and min values from 't1'
"""
t1 = (1,2,7,9,2,4,6,8,10)
half = len(t1) // 2
print("First half: ", t1[:half])
print("Second half: ", t1[half:])

evenTuple = tuple(x for x in t1 if x % 2 == 0)
print("Even tuple: ", evenTuple)

t2 = (11,13,15)
concatenatedTuple = t1 + t2
print("Concatenated Tuple: ", concatenatedTuple)

print("Max: ", max(t1), "Min: ", min(t1))
