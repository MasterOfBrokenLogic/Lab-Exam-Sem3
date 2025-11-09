"""
A function that takes a sentence as input from the user and calculates the frequency of each letter.
Use a variable of dictionary type to maintain the count.
"""
def letterFreq(sentence):
    freq = {}
    for ch in sentence:
        if ch.isalpha():
            ch = ch.lower()
            freq[ch] = freq.get(ch, 0) + 1
    return freq

text = input("Enter the sentence: ")
frequencies = letterFreq(text)

print("\nLetter Frequencies:")
for letter, count in sorted(frequencies.items()):
    print(f"{letter}: {count}")
