import csv

records = []
headings = []


def load_data(file_path):
    print("Loading data...")
    with open(file_path) as file:
        reader = csv.reader(file)
        headings.append(next(reader))
        for row in reader:
            records.append(row)
    print("Done!")


def run():
    load_data("E:/pycharmprojects/week6/titanic/titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records")


run()
