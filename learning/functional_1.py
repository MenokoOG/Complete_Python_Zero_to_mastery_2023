"""Functional Programming, L. Jefferson II, Menoko OG, 11/2023"""
# Pure Functions equals less buggy code. This is a guideline, not a rule. Data and functions are separate in program.
# functions should always produce same output when same input given, no matter how many times ran. functions should have no side effects on outside world or scope of function.
def multiply_by2(li): #good function design. Pure function!!!!
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))

print("*" * 40)

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return print(new_list) #here is interacts wiht outside world, it prints when it is to be a multiply function. so, this is not good practice

multiply_by2([1,2,3])

print("*"* 40)

new_list = [] #here this is outside world, outside scope of function, not good practice. 
def multiply_by2(li):
    
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))