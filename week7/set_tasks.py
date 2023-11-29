def observed():
    observation = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observation


def run_task1():
    print(observed())


run_task1()


def observed_items():
    observations = []
    for count in range(0, 7):
        print("Please enter an observation:")
        observations.append(input())
    return observations


def run_task2():
    print("Counting observations...")
    observations = observed()
    empty_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        empty_set.add(data)

    for data in empty_set:
        print(f"{data[0]} observed {data[1]} times.")


