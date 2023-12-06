"""Decorator lesson, L. Jefferon II, Menoko OG, 11/2023"""
# def hello():
#     print("hellllllooooooo")

# greet = hello
# del hello #even though the hello function is deleted from memory, greet still points to it.

# #functions are just like variables, they are first class citizens.
# print(greet())
def hello(func):# HOF
    func()

def greet():
    print("still here!")

a = hello(greet)

print(a)
print("*" * 40)
#Higher order function HOF is a function that accepts another functions as it parameters like the hello function above or a function that returns another function
def greet2():
    def func():
        return 5
    return func
