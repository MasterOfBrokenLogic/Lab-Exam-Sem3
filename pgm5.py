"""
Creating a menu driven program to perform the following operations on strings using built-in string functions!
  a) Find the frequency of a character from a string
  b) Replace a charcter by another character in a string
  c) Remove the first occurance of a character in a string
  d) Remove all the occurance of a character from a string
"""
def stringOps():
    string = input("Enter the string: ")

    while True:
        print("\n1. Find frequency of a char in the string.")
        print("2. Replace a char by another char.")
        print("3. Remove the first occurrence of a string.")
        print("4. Remove all occurrences of a string.")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            ch = input("Enter the character to find its frequency: ")
            freq = string.count(ch)
            print(f"The frequency of '{ch}' in the string is: {freq}")

        elif choice == 2:
            oldChar = input("Enter the character to replace: ")
            newChar = input("Enter the new character: ")
            updatedString = string.replace(oldChar, newChar)
            print("Updated String is:", updatedString)
            string = updatedString

        elif choice == 3:
            char = input("Enter the character to remove (first occurrence): ")
            if char in string:
                updatedString = string.replace(char, "", 1)
                print("Updated String is:", updatedString)
                string = updatedString
            else:
                print(f"The character '{char}' is not in the string.")

        elif choice == 4:
            char = input("Enter the character to remove all occurrences: ")
            updatedString = string.replace(char, "")
            print("Updated String:", updatedString)
            string = updatedString

        elif choice == 5:
            print("Exiting the program!")
            break

        else:
            print("Invalid choice! Please select a valid option!")

stringOps()
