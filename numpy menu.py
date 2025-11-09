"""
Using numpy module to write a menu-driven program to do the following:
  a) Create an array filled with 1's
  b) Find the Max & Min values from an array
  c) Dot product of 2 arrays
  d) Reshape 1D array to 2D array
"""
import numpy as np


def numpyMenu():

    while True:
        print("\n1. Print in 1`s")
        print("2. Find max and min from an array!")
        print("3. Find the dot product of 2 numbers!")
        print("4. Reshape 1d array to 2d array")
        print("5. Exit!")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter the size: "))
            print(np.ones(n, dtype=int))

        elif choice == 2:
            arr = np.array(list(map(int, input("Enter the array: ").split())))
            print("Min: ", arr.min(), "Max: ", arr.max())

        elif choice == 3:
            str1 = int(input("Enter the first element: "))
            str2 = int(input("Enter the second element: "))
            print(np.dot(str1, str2))

        elif choice == 4:
            arr = np.array(list(map(int, input("Enter the arrray: ").split())))
            row = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            if row * cols == arr.size:
                print(arr.reshape(row, cols))
            else:
                print("Reshaping is not possible!")

        elif choice == 5:
            break


numpyMenu()
