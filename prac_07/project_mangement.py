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
    """Load and save a data file and use a list of Project objects"""
    projects = load_project(FILENAME)
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("filename: ")
            projects = load_project(filename)
        elif choice == "s":
            filename = input("filename: ")
            save_project(filename, projects)
        elif choice == "d":
            display(projects)
        elif choice == "f":
            filter_project(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("error")
        print(MENU)
        choice = input(">>> ").lower()
    save_project(FILENAME, projects)
    print("Thank you for using custom-built project management software.")

def load_project(filename):
    """Loads a projects from a file"""
    projects = []
    with open(filename, "r", encoding="utf8") as in_file:
        in_file.readline()
        for line in in_file:
            project_bits = line.strip("\n").split("\t")
            project_bits[INDEX_PRIORITY] = int(project_bits[INDEX_PRIORITY])
            project_bits[INDEX_COST_ESTIMATE] = float(project_bits[INDEX_COST_ESTIMATE])
            project_bits[INDEX_COMPLETION_PERCENTAGE] = int(project_bits[INDEX_COMPLETION_PERCENTAGE])
            project_bits[INDEX_START_DATE] = datetime.datetime.strptime(project_bits[INDEX_START_DATE],
                                                                        "%d/%m/%Y").date()
            projects.append(
                Project(project_bits[INDEX_NAME], project_bits[INDEX_START_DATE], project_bits[INDEX_PRIORITY],
                        project_bits[INDEX_COST_ESTIMATE], project_bits[INDEX_COMPLETION_PERCENTAGE]))
        return projects


def save_project(filename, projects):
    """saves a project to a file"""
    with open(filename, "w", encoding="utf8") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion\tPercentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display(projects):
    """Displays projects in order of priority and splits them by completion"""
    print("Incomplete projects:")
    for project in (project for project in sorted(projects) if not project.is_complete()):
        print(f"\t{project}")
    print("Completed projects:")
    for project in (project for project in sorted(projects) if project.is_complete()):
        print(f"\t{project}")


def filter_project(projects):
    """Displays projects after an inputted date"""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in (project for project in sorted(projects) if project.start_date >= filter_date):
        print(project)


def add_project(projects):
    """Add a new project"""
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    complete_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, complete_percentage))


def update_project(projects):
    """Updates the projects' completion percentage and/or priority"""
    for i, project in enumerate(projects):
        print(i, project)
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_percentage = input("New Percentage: ")
    if new_percentage != "":
        project.completion_percentage = int(new_percentage)
    new_priority = input("New Priority: ")
    if new_priority != "":
        project.priority = int(new_priority)


main()
