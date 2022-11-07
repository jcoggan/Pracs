from guitar import Guitar

FILENAME = "guitars.csv"
guitars = []
with open(FILENAME, "r+", encoding="utf8") as guitar_file:
    for line in guitar_file:
        guitar_parts = line.strip().split(",")
        guitar = Guitar(guitar_parts[0], int(guitar_parts[1]), float(guitar_parts[2]))
        guitars.append(guitar)
    print("Current Guitars")
    for guitar in sorted(guitars):
        print(guitar)

    print("New Guitars")
    name = input("Name: ")
    if name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added")
        name = input("Name: ")

    guitar_file.seek(0)
    for guitar in guitars:
        print(f"{guitar.name}, {guitar.year}, {guitar.cost}", file=guitar_file)
    guitar_file.truncate()
