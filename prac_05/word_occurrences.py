"""
Word Occurrences
Estimate: 30 minutes
Actual: ? minutes
"""

word_to_occurrences = {}
text = input("Text: ")
for word in text.split(" "):
    if word in word_to_occurrences:
        word_to_occurrences[word] = word_to_occurrences[word] + 1
    else:
        word_to_occurrences[word] = 1

for word in word_to_occurrences:
    print(f"{word} : {word_to_occurrences[word]}")