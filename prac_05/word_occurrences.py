"""
Word Occurrences
Estimate: 30 minutes
Actual: 18 minutes
"""

word_to_occurrences = {}
longest_word_length = 0
text = input("Text: ")
for word in text.split(" "):
    if word in word_to_occurrences:
        word_to_occurrences[word] += 1
    else:
        word_to_occurrences[word] = 1
    if len(word) > longest_word_length:
        longest_word_length = len(word)

for word in sorted(word_to_occurrences):
    print(f"{word:{longest_word_length}} : {word_to_occurrences[word]}")
