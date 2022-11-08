import datetime
from prac_07.project import Project

MENU = " - (L)oad projects\n - (S)ave projects\n - (D)isplay projects\n - (F)ilter projects by date\n" \
       " - (A)dd new project\n - (U)pdate project\n - (Q)uit"
FILENAME = "project.txt"
INDEX_NAME = 0
INDEX_START_DATE = 1
INDEX_PRIORITY = 2
INDEX_COST_ESTIMATE = 3
INDEX_COMPLETION_PERCENTAGE = -1


def main():
    projects = []
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            # filename = input("filename: ")
            filename = "project.txt"
            projects = load_project(filename)
        elif choice == "s":
            # filename = input("filename: ")
            filename = "project.txt"
            save_project(filename, projects)
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
    """Loads a projects from a file"""
    projects = []
    with open(filename, "r", encoding="utf8") as in_file:
        in_file.readline()
        for line in in_file:
            project_bits = line.strip("\n").split("\t")
            # project_bits[INDEX_START_DATE] = datetime.datetime.strptime(project_bits[INDEX_START_DATE],
            #                                                             "%d/%m/%Y").date()
            projects.append(Project(project_bits[INDEX_NAME], project_bits[INDEX_START_DATE], project_bits[INDEX_PRIORITY],
                        project_bits[INDEX_COST_ESTIMATE], project_bits[INDEX_COMPLETION_PERCENTAGE]))
        return projects


def save_project(filename, projects):
    """saves a project to a file"""
    with open(filename, "w", encoding="utf8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion\tPercentage", file=out_file)
        for project in projects:
            print(project, file=out_file)


def display():
    pass


def filter_project():
    pass


def add_project():
    pass


def update_project():
    pass


main()
