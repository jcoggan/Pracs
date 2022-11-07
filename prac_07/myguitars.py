from guitar import Guitar

FILENAME = "guitars.csv"
guitars = []
with open(FILENAME, "r", encoding="utf8") as in_file:
    for line in in_file:
        guitar_parts = line.strip().split(",")
        guitar = Guitar(guitar_parts[0], int(guitar_parts[1]), float(guitar_parts[2]))
        guitars.append(guitar)

for guitar in sorted(guitars):
    print(guitar)