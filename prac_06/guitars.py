from guitar import Guitar


def main():
    guitars = []
    # test guitars
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # longest_name = 20
    # longest_cost_character_length = 10
    got_all_guitars = False
    longest_name = 0
    longest_cost_character_length = 0
    while not got_all_guitars:
        name = input("Name: ")
        if name != "":
            if len(name) > longest_name:
                longest_name = len(name)
            year = int(input("Year: "))
            cost = int(input("Cost: "))
            if len(str(cost)) > longest_cost_character_length:
                longest_cost_character_length = len(str(cost))
            guitars.append(Guitar(name, year, cost))
            print(f"{name} ({year}) : ${cost} added")
        else:
            got_all_guitars = True
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print(f"Guitar {i}: {guitar.name:>{longest_name}} ({guitar.year}), worth $ "
              f"{guitar.cost:>{longest_cost_character_length},.2f} {vintage_string}")


main()
