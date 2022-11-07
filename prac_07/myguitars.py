from prac_06.guitar import Guitar
from operator import itemgetter

FILENAME = "guitars.csv"
guitars = []
with open(FILENAME, "r", encoding="utf8") as in_file:
    for line in in_file:
        guitar_parts = line.strip().split(",")
        guitar = Guitar(guitar_parts[0], int(guitar_parts[1]), float(guitar_parts[2]))
        guitars.append(guitar)