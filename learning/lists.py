"""List lessons, L. Jefferson II "Menoko OG, 11/2023"""
#list slicing
my_cart = ["laptop", "phone", "shoe", "gum"]
new_cart = my_cart[:] # a copy of my_cart

new_cart[0] = "desktop"
sort_cart = sorted(my_cart)

print(my_cart)
print(new_cart)
print(sort_cart)
print(my_cart[::-1])

"""Matrix, below is two dimensional as it has a list within a list, put another list within the second list and it would be three dimensional, array like"""
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
print(matrix[0])
print(matrix[1])
print(matrix[2] [1])
print(matrix[0] [2])
print("*" * 30)
matrix2 = [
    [[1,2,3],2, 3],
    [4,5,6],
    [7,8,9]
]
print(matrix2[0][0][2]) #three dimesional reference