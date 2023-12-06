"""Lambda functions, L. Jefferson II, Menoko OG, 11/2023"""
#lambda functions or expressions- one time functions
from functools import reduce

my_list = [1,2,3]

# def multiply_by2_new(item):
#     return item * 2

# def only_odd(item):
#     return item % 2 != 0

# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item
    
#lambda made it possible to not even have to use functions
print(list(map(lambda item : item * 2, my_list)))
print(list(filter(lambda item : item % 2 != 0, my_list)))
print(reduce(lambda acc, item : acc + item, my_list))
print(my_list)