# Activity 1
def display_ladder(steps):
    for steps in range(steps):
        print("| |")
        print("***")
        print("| |")


def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)


create_ladder()


# Activity 2
def sum_weights(chr_weight, inv_weight):
    total = chr_weight + inv_weight
    return total


def calc_avg_weight(chr_weight, inv_weight):
    avg_weight = sum_weights(chr_weight, inv_weight) / 2
    return avg_weight


def run():
    print("What is the weight of the person?")
    chr_weight = float(input())
    print("What is the weight of their inventory?")
    inv_weight = float(input())
    print("What would you like to calculate (sum or average)?")
    answer = input()
    if answer == "sum":
        print(f"The sum of weights is {sum_weights(chr_weight, inv_weight)}.")
    elif answer == "average":
        print(f"The average of weights is {calc_avg_weight(chr_weight, inv_weight)}")


run()
