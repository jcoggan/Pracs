"""
Menus

pseudocode:
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

def main():
    """respond to user using inputted name based on choice form menu"""
    name = input("Name: ")
    get_choice(name)
    print("FInished")


def get_choice(name):
    """Responds to user based on input"""
    print_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"goodbye {name}")
        else:
            print("invalid message")
        print_menu()
        choice = input(">>> ").upper()


def print_menu():
    """Displayes menu"""
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


main()