"""
wimbledon
Estimate: 50 minutes
Actual: 41.5 minutes
"""
FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    records = get_records()
    champion_to_wins, countries = process_records(records)
    display_processed_records(champion_to_wins, countries)


def get_records():
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    countries = set()
    champion_to_wins = {}
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_wins[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_wins[record[CHAMPION_INDEX]] = 1
    return champion_to_wins, countries


def display_processed_records(champion_to_wins, countries):
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(champion, wins)
    print(f"\nThese {len(countries)} countries have won wimbledon:")
    print(",".join(sorted(countries)))


main()
