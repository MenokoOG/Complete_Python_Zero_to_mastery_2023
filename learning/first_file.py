print("""***********************************
First File of Udemy Python Developer Course, L. Jefferson II "Menoko OG 11-2023
***********************************""")
# f string or formatted string in where tou can use placement of variables.
name = "LJ"
age = 28
print(f"your name is {name} and you are {age} years old.")
print("Your name is {} and your are {} years old.".format(name, age)) #python 2 format style
print("*" * 30)
def greet():
    a = input("what is your first name? ")
    b = input("What is your age? ")
    c = a.title() #here is to capitalize the input name.
    # print(a.title())
    # print(b)
    print(f"Hello, your name is {c} and you are {b} years old.")
greet()
print("*" * 20)
