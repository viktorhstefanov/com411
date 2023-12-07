import json


def read(file_path):
    with open(file_path) as file:
        data = json.load(file)
        location = data["location"]
        pop_size = data["population"]
        print(f"Place Name: {location}")
        print(f"Population Size: {pop_size}")
        bots = data["bots"]
        for bot in bots:
            bot_name = bot["name"]
            stats = bot["stats"]
            print(f"{bot_name} has the following stats: {stats}")


def run():
    read("futarama.json")


if __name__ == "__main__":
    run()
