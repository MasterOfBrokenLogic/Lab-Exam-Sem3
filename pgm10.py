"""
Write a fn that reads a file 'file1' and copies all alternative lines to another file 'file2'.
The lines copied should be the odd-numbered lines.
"""
def copy(file1, file2):
    with open(file1, "r") as f1, open(file2, "w") as f2:
        lines = f1.readlines()
        for i in range(0, len(lines), 2):
            f2.write(lines[i])

copy("input.txt", "output.txt")

"""
    Create another file named input.txt and write any things:
    for eg: 
        Apple
        Banana
        Cherry
        Dragonfruit
        Elderberry
        Fig
        Grapes
        Honeydew
        Indian Fig
        Jackfruit
"""
