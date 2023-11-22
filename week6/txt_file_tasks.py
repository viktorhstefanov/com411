import os


def cwd():
    path = os.getcwd()
    print(f"Current Working Directory: {path}")
    print("The directory contains the following files:")
    for file in os.listdir(path):
        print(file)


def run():
    print("Processing...")
    cwd()


run()


def display_chars(file_path, charnum):
    with open(file_path) as file:
        data = file.read(charnum)
        print(f"The first {charnum} characters are:")
        print(data)


def display_line(file_path):
    with open(file_path) as file:
        data = file.readline().strip()
        print("The first line is:")
        print(data)


def display_text(file_path):
    print("The full text is:")
    with open(file_path) as file:
        content = file.read()
        print(content)


def run_task2():
    display_chars("E:/pycharmprojects/week6/library.txt", 5)
    display_line("E:/pycharmprojects/week6/library.txt")
    display_text("E:/pycharmprojects/week6/library.txt")


run_task2()


def search(file_name):
    print("Searching...")
    with open(file_name) as file:
        for location in file:
            print(f"Looked in {location.strip()}")
    print("...Done!")


def run_task3():
    search("E:/pycharmprojects/week6/library.txt")


run_task3()


def search_books(file_path):
    print("Searching...")
    sections = " "
    books = "Books:\n"
    with open(file_path) as file:
        for line in file:
            if line.startswith('Section:'):
                sections += line
            else:
                books += line
    print("Done!")
    print(sections)
    return f"{sections}\n\n{books}"


def save(file_path, data_string):
    print("Saving...")
    with open(file_path, "w") as file:
        file.write(data_string)
    print("Done!")


def run_task4():
    data = search_books("E:/pycharmprojects/week6/library.txt")
    save("E:/pycharmprojects/week6/section-books.txt", data)


run_task4()


