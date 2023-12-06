"""Generator lesson, L. Jefferson II, Menoko OG, 11/2023"""
#fibonacci number
def fib(number):
    a, b = 0, 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(20):
    print(x)

print("*" * 40)
def fib2(number): #list way to do it
    a, b = 0, 1
    result = []
    for i in range(number):
        result. append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fib2(20))