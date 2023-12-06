"""Set lesson, L. Jefferosn II, Menoko OG, 11/2023"""
# my_set = {1,2,3,4,5} #in set there are no duplicate items, there can be only one!
# print(my_set)
# my_set.add(100)
# print(my_set)
# my_list = [1,2,3,4,5,5]
# print(set(my_list)) #this will take any duplicates out of original list
my_set = {1,2,3,4,5}
small_set = {4,5}
your_set = {4,5,6,7,8,9,10}

# print(my_set.difference(your_set))
# print(my_set.discard(5))
# print(my_set)
# print(my_set.difference_update(your_set))
# print(my_set)
# print(my_set.intersection(your_set))
print(my_set & your_set) #shorthand for intersection
print(my_set.union(your_set))
print(my_set | your_set) #shorthand for union
print(my_set.isdisjoint(your_set)) #will return false because the compared sets do in fact have common values.
print(small_set.issubset(your_set))
print(your_set.issuperset(small_set))

#some useful methods
# .differnce()
# discard()
# .difference_update()
# .intersection()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union()