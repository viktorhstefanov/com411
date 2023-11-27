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
  [5] Display the number of survivors per age group
  """)
    response = int(input())
    return response


def display_passenger_names():
    print("The names of the passengers are...")
    for record in records:
        passenger_name = record[3]
        print(passenger_name)


def display_num_survivors():
    num_survived = 0
    for record in records:
        survival_status = int(record[1])
        if survival_status == 1:
            num_survived += 1
        else:
            pass
    print(f"{num_survived} passengers survived.")


def display_passengers_per_gender():
    females = 0
    males = 0
    for record in records:
        if record[4] == "male":
            males += 1
        elif record[4] == "female":
            females += 1
    print(f"females: {females}, males: {males}")


def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    for record in records:
        if record[5] != "":
            age = float(record[5])
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1

    print(f"children: {children}, adults: {adults}, elderly: {elderly}")


def display_survivors_per_age_group():
    children = adults = elderly = 0
    child_survivor = adult_survivor = elderly_survivor = 0

    for record in records:
        num_survived = int(record[1])
        if record[5] != "":
            age = float(record[5])
            if age < 18:
                children += 1
                if num_survived == 1:
                    child_survivor += 1
            elif age < 65:
                adults += 1
                if num_survived == 1:
                    adult_survivor += 1
            else:
                elderly += 1
                if num_survived == 1:
                    elderly_survivor += 1
    print(
        f"children: {child_survivor}/{children}, adults: {adult_survivor}/{adults}, elderly: {elderly_survivor}/{elderly}")


def run():
    load_data("E:/pycharmprojects/week6/titanic/titanic.csv")
    num_records = len(records)
    print(f"Successfully loaded {num_records} records")

    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")

    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
        display_passengers_per_gender()
    elif selected_option == 4:
        display_passengers_per_age_group()
    elif selected_option == 5:
        display_survivors_per_age_group()
    else:
        print("Error! Option not recognised!")


run()
