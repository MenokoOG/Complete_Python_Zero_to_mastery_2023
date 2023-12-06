"""Tuple , L. Jefferosn II, Menoko OG 11/2023"""
my_tuple = (1,2,3,4,5) #immutable
print(5 in my_tuple)
user = {
    (1,2) : [1,2,3], #tuple can by used as key in dictionary
    "greet" : "hello",
    "age" : 20
}
print(user[(1,2)])

new_tuple = my_tuple[1:2]
print(new_tuple)
x, y, z, *other = (1,2,3,4,5)
print(z)
print(other)
my_tuple = (1,2,3,4,5)
print(my_tuple.count(2)) # how many of arguement in tuple
print(my_tuple.index(4)) #position of arguement value in tuple
print(len(my_tuple))