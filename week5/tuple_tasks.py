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


# Activity 3
def steps():
    likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
    return likelihoods


def run_task3():
    likelihood1 = steps()
    good_steps = []
    bad_steps = []
    for item in likelihood1:
            if item[1] >= 50:
                good_steps.append(item)
            elif item[1] <= 50:
                bad_steps.append(item)
    print(f"Good steps: {len(good_steps)}, Bad steps {len(bad_steps)}")


run_task3()



