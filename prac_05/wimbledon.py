"""
wimbledon
Estimate: 50 minutes
Actual: ? minutes
"""
# Year	Country	Champion	Country	Runner-up	Score in the final
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


main()
