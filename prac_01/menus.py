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

name = input("Name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
       print(f"Hello {name}")
    elif choice == "G":
       print(f"goodbye {name}")
    else:
       print("invalid message")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>> ").upper()
print("FInished")
