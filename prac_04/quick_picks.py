import random

MAX_NUMBER = 45
MIN_NUMBER = 1
NUMBER_OF_NUMBERS = 6

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(NUMBER_OF_NUMBERS):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in quick_pick:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick.append(number)
    print(" ".join(f"{number:2}" for number in sorted(quick_pick)))
