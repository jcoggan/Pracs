"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    while score > 100 or score < 0:
        print("Invalid score")
        score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    score = random.randint(0, 100)
    result = determine_result(score)
    print(result)



def determine_result(score):
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    return "Excellent"


main()