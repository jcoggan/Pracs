"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# Original
score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
    print("Excellent")
if score < 50:
    print("Bad")

# Fixed
score = float(input("Enter score: "))
while score > 100 or score < 0:
    print("Invalid score")
    score = float(input("Enter score: "))
if score < 50:
    print("Bad")
elif score < 90:
    print("Pass")
else:
    print("Excellent")