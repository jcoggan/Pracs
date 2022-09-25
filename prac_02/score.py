"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

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