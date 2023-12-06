"""Functional Programming, L. Jefferson II, Menoko OG, 11/2023"""
# map, filter, zip, and reduce
from functools import reduce
def multiply_by2(li): 
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list
print(map(multiply_by2, [1,2,3])) #creates object in memory

print("*" * 40)
#using map to simplify function, good for iterating over data
my_list = [1,2,3]
def multiply_by2_new(item):
    return item * 2

print(list(map(multiply_by2_new, [1,2,3]))) #map calls function, why no () to call
print(list(map(multiply_by2_new, my_list))) #creates new list from my_list without changing my_list global
print(my_list)
print("*" * 40)

#filter , as it suggustes it will filter occording to conditional 
my_list = [1,2,3]
def multiply_by2_new(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))
print(my_list)
print("*" * 40)

#zip, puts iterables together
my_list = [1,2,3]
your_list = (10,20,30)
their_list = (5,4,3)
def multiply_by2_new(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0

print(list(zip(my_list, your_list, their_list)))
print(my_list) 

print("*" * 40)
#reduce have to import form functools module- Python's reduce() is a function that implements a mathematical technique called folding or reduction. reduce() is useful when you need to apply a function to an iterable and reduce it to a single cumulative value
my_list = [1,2,3]

def multiply_by2_new(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item
    

print(reduce(accumulator, my_list, 0))
print(my_list) 
