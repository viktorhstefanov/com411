import csv


def read_csv(file_path):
    with open(file_path) as file:
        reader = csv.reader(file)
        headings = next(reader)
        print(f"Headings:\n{headings}")
        print("Values:")
        for row in reader:
            print(row)


def run_task1():
    read_csv("E:/pycharmprojects/week6/clothing.csv")


run_task1()


def function(file_path):
    print("Extracting...")
    with open(file_path) as file:
        reader = csv.reader(file)
        headings = next(reader)
        names = ""
        for row in reader:
            names += f"{row[1]}\n"
    print(f"Done! The extracted items are as follows:\n{names}")


def run_task2():
    function("E:/pycharmprojects/week6/clothing.csv")


run_task2()


def export(file_path, item_num):
    print("Exporting...")
    with open(file_path, "a") as file:
        for count in range(item_num):
            print("Enter the item id:")
            item_id = input()
            print("Enter the item name:")
            item_name = input()
            print("Enter the item colour:")
            item_colour = input()
            content = f"{item_id},{item_name},{item_colour}\n"
            file.write(content)
    print("Done!")



def run_task3():
    export("E:/pycharmprojects/week6/clothing.csv", 2)


run_task3()




