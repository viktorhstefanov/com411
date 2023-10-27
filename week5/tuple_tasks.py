# Activity 1
def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)


def run_task1():
    value = likelihood()
    print(f"Minimum likelihood of falling: {value}%")


run_task1()


# Activity 2
def likelihood_min_max():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def run_task2():
    value = likelihood_min_max()
    print(f"Minimum likelihood of falling: {value[0]}%")
    print(f"Maximum likelihood of falling: {value[1]}%")


run_task2()

