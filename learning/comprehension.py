"""Comprehension lesson, L. Jefferson II, Menoko OG, 11/2023"""
#list, set, dictionary comprhension
# my_list = [char for char in "hello"]
# my_list2 = [num for num in range(0,100)]
# my_list3 = [num * 2 for num in range(0,100)]
# my_list4 = [num * 2 for num in range(0,100) if num % 2 == 0]
# my_odd_list = [num for num in range(0,100) if num % 2 ==1]

# print(my_list)
# print(my_list2)
# print(my_list3)
# print(my_list4)
# print(my_odd_list)
# #for set 
print("*" * 40)
# my_list = {char for char in "hello"} #here will only print one l because sets can only have one unique item
# my_list2 = {num for num in range(0,100)}
# my_list3 = {num * 2 for num in range(0,100)}
# my_list4 = {num * 2 for num in range(0,100) if num % 2 == 0}
# my_odd_list = {num for num in range(0,100) if num % 2 ==1}

# print(my_list)
# print(my_list2)
# print(my_list3)
# print(my_list4)
# print(my_odd_list)
print("*" * 40)
# for dictionary
simple_dict = {
    "a" : 1,
    "b" : 2
}
# my_dict = {key:value ** 2 for key, value in simple_dict.items()}
# my_dict = {k:v ** 2 for k, v in simple_dict.items() if v % 2 ==0} # same as above jusy key, value shortened
my_dict = {num:num * 2 for num in [1,2,3]}

print(my_dict)