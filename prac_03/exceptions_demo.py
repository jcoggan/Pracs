"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    ValueError will occur when numerator or denominator are not a number or if input is a float.
2. When will a ZeroDivisionError occur?
    ZeroDivisionError will occur when the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    not sure
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")