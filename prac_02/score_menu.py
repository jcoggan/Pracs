def main():
    """Gets a score then can show result and print stars"""
    score = get_valid_score()
    print_menu()
    choice = input("Choice: ").lower()
    while choice != "q":
        if choice == "r":
            result = determine_result(score)
            print(result)
        elif choice == "s":
            print("*" * int(score))
        else:
            print("Invalid choice")
        choice = input("Choice: ").lower()

def print_menu():
    """Display menu"""
    print("what would you like to do with your score?")
    print("R to display result")
    print("S to print a star for every point of score")


def get_valid_score():
    """get a valid score"""
    score = float(input("Enter score: "))
    while score > 100 or score < 0:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_result(score):
    """determine the results based on the score"""
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    return "Excellent"


main()