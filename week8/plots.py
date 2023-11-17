import matplotlib.pyplot as plt


def display_line(x, y):
    plt.plot(x, y)
    plt.show()


def run_task1():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    display_line(x_values, y_values)


run_task1()


def small():
    x = [3, 4, 4, 3, 3]
    y = [3, 3, 4, 4, 3]
    plt.plot(x, y, 'ro:')


def medium():
    x = [2, 5, 5, 2, 2]
    y = [2, 2, 5, 5, 2]
    plt.plot(x, y, 'gs:')


def large():
    x = [1, 6, 6, 1, 1]
    y = [1, 1, 6, 6, 1]
    plt.plot(x, y, 'bp-')


def run_task2():
    small()
    medium()
    large()
    plt.show()


run_task2()


def coordinate():
    print("Please enter a x value")
    x = int(input())

    print("Please enter a y value")
    y = int(input())
    return (x, y)


def path():
    print("Retrieving path...")
    x_values = []
    y_values = []

    for count in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
        return [x_values, y_values]

def run_task3():
    values = path()
    plt.plot(values[0], values[1], 'r--')
    plt.show()

run_task3()
