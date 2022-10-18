"""
Word Occurrences
Estimate: 30 minutes
Actual: ? minutes
"""

words = {}
text = input("Text:")
for word in text.split(" "):
    if word in words:
        words[word] = words[word] + 1
    else:
        words[word] = 1
print(words)