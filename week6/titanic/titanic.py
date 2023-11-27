import csv

records = []
headings = []


def load_data(file_path):
    print("Loading data...", end="")
    with open(file_path) as file:
        reader = csv.reader(file)
        headings.append(next(reader))
        for row in reader:
            records.append(row)
    print("Done!")


def display_menu():
    print("""
  Please select one of the following options:
  [1] Display the names of all passengers
  [2] Display the number of passengers that survived
  [3] Display the number of passengers per gender
  [4] Display the number of passengers per age group
  """)
    response = int(input())
    return response


def run():
    load_data("E:/pycharmprojects/week6/titanic/titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records")

    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")


run()