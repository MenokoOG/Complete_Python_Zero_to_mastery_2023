"""GUI Exercise, L. Jefferson II, Menoko OG, 11/2023"""
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for row in picture:
    for pixel in row:
        if pixel == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
#clean
# readability
# predictability
# DRY-Don't Repeat Yourself
print("*" * 40)
#cleaner way of doing the same program
fill = "*"  #this way if you want to use differrent symbol, it only has to be changed in one place in the code.
empty = " "
for row in picture:
    for pixel in row:
        if pixel:
            print(fill, end="")
        else:
            print(empty, end="")
    print("")