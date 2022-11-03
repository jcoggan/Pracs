import datetime
from prac_07.project.py import Project

MENU = " - (L)oad projects\n - (S)ave projects\n - (D)isplay projects\n - (F)ilter projects by date\n" \
       " - (A)dd new project\n - (U)pdate project\n - (Q)uit"
FILENAME = "project.txt"


def main():
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            load_project(filename)
        elif choice == "s":
            save_project()
        elif choice == "d":
            display()
        elif choice == "f":
            filter_project()
        elif choice == "a":
            add_project()
        elif choice == "u":
            update_project()
        else:
            print("error")
        choice = input(">>> ").lower()


def load_project(filename):
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:




main()
