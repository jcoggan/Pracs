"""
wimbledon
Estimate: 50 minutes
Actual: ? minutes
"""
FILENAME = "wimbledon.csv"


def main():
    records = get_records()
    for record in records:
        print(record)


def get_records():
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
