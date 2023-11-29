def pattern1():
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences


def display_keys(data):
    for key in data:
        print(key)


def display_values(data):
    for value in data.values():
        print(value)


def display_items(data):
    for item in data.items():
        print(item)


def run():
    data = pattern1()
    print("Dictionary:")
    print(data)
    print()
    print("Keys:")
    display_keys(data)
    print()
    print("Values:")
    display_values(data)
    print()
    print("Pairs:")
    display_items(data)


run()


def short_pattern():
    pattern = {"sequence": "101", "occurrences": 5}
    return pattern


def medium_pattern():
    pattern = {"sequence": "111000", "occurrences": 25}
    return pattern


def long_pattern():
    pattern = {"sequence": "1100110011001100", "occurrences": 50}
    return pattern


def run_task3():
    print("Analysing patterns...")
    patterns = {"short sequence": short_pattern(), "medium sequence": medium_pattern(), "long sequence": long_pattern()}
    for key, value in patterns.items():
        print(f"{key}: {value}")


run_task3()