"""scope lesson, L. Jefferson II, Menoko OG, 11/2023"""
#what varaiables do you have access to.
# think of functional scope as each function is its own world and variables within are only used within that world, whereas global variables can be used by the universe.

guns = "all guns" #global variable

print(f" {guns} is global variable")

def get_guns():
    this_gun = "ak47" #variable that can only be used inside this function
    print(f" {this_gun} is inside function")
    print(f" this {guns} can still be used inside because of global")
get_guns()
# print(this_gun) #this causes error because this gun cannot be used outside it's own world.
print("*" * 40)
total = 0

# def count():
#     global total #so the global varaible can be used and defined in function
#     total += 1
#     return total
# count()
# count()
# print(count())
print("*" * 40)
#better way to do this is injection of global variable as param of function.
def count2(total):
    total += 1
    return total

print(count2(count2(count2(count2(total)))))
print("*" * 40)
# scope is useful becasue of machine resource management
def outer():
    x = "local"
    def inner():
        # nonlocal x
        x = "nonlocal"
        print("inner:", x)
        
    inner()
    print("outer:", x)
    
outer()

