# *args and **kwags, being able to pass in multiple arguements and the keyword arguements into function.
def super_func(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))

#rule: params, *args, defaault params, **kwargs, this is order of position within passing in arguements in functions
# example:
# def rule_func (name, *args, i="hi", **kwargs): 