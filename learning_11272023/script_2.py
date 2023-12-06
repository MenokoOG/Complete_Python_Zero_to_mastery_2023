"""I/O lesson file, correct way to open files, Menoko OG, 11-2023"""
try:
    with open('test.txt', mode="r+") as my_file:
        print(my_file.readlines())
except FileNotFoundError as err:
    print("File does not exist")
    raise err

try: # good practice to wrap operation in try in case file does nto exist.
    with open('potato.txt', mode="r+") as my_file:
        print(my_file.readlines())
except FileNotFoundError as err:
    print("File does not exist")
    raise err