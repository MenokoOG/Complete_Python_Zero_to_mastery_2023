"""Decorator lesson, L. Jefferson II, Menoko OG, 11/2023"""
def my_decorator(func):
    def wrap_func():
        print("***************")
        func()
        print("***************")
    return wrap_func

@my_decorator
def hello():
    print("Helllloooooo")

@my_decorator
def bye():
    print("see ya later alligator")

hello2 = my_decorator(hello) #under the hood this is what the @ decorator is basically doing.
    
hello()
bye()
hello2()
print("*" * 40)
#decorator pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("Decorator Action function is getting wrapped !!!!")
        func(*args, **kwargs)
        print("Decorator Action, function is wrapped!!!!")
    return wrap_func

@my_decorator
def hello(greeting, emoji=":)"):
    print(greeting, emoji)
hello("hiiiii")