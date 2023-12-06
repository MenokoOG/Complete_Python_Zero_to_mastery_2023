"""functions, L. Jefferson II, Menoko OG, 11/2023"""
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

fill = "*"  
empty = " "
def show_tree():
    for row in picture:
        for pixel in row:
            if pixel:
                print(fill, end="")
            else:
                print(empty, end="")
        print("")
print(show_tree) #shows where function is stored in memory
show_tree()
print("*" * 40)
#return 
# def sum(num1, num2):
#      return num1 + num2
# print(sum(4,5))
# #function should do one ting really well
# #should return something.
# total = sum(10,5)
# print(sum(10, total))
print("*" * 40)
def sum(num1, num2):
    def another_func(num1, num2):
        return num1 + num2
    return another_func(num1, num2)

total = sum(10,20)
print(total)
print("*" * 40)
#doc strings
def greet():
    """this is a greet function""" #when you hover over function this wil show up.
    print("hello")
    

greet()
print(greet.__doc__)
print("*" * 40)


