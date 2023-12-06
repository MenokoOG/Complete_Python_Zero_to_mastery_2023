"""Dictionary in python, L. Jefferson II, Menoko OG 11/2023"""
dictionary = { 
              "weapons": [1,2,3], 
              "greeting" : "hello", 
              "is_magic" : True
}
print(dictionary["weapons"])
print(dictionary["greeting"])
print(dictionary["weapons"] [2])
print(dictionary["is_magic"])

print("*" * 30)
# this would be an array type structure a list of dictionaries, lists are ordered by index and value, where as dictionaries can contain lot more information by keys, keys are immutable and have to be unique
my_list = [{ 
              123: [1,2,3], 
              True : "hello", 
              "x" : True
},
{ 
              "a": [4,5,6], 
              "b" : "hello", 
              "x" : True
}]

print(my_list[0][123])
print(my_list[0][True])
print(my_list[1]["a"][1])
print("*" * 30)
user = {
    "basket" : [1,2,3],
    "greet" : "hello"
}

print(user.get("age")) #the key is not in dictionary, but will not stop program; does not raise error
print(user.get("age", 55)) #this asigns a value if key does not exist in dictionary
user2 = dict(name= "johnjohn", age= 40) #another way to create dictionary
print(user2)
print(user2["name"])
print(user2["age"])
print("*" * 30)
user = {
    "basket" : [1,2,3],
    "greet" : "hello",
    "age" : 20
}
print("basket" in user)
print("size" in user)
print("age" in user.keys())
print("hello" in user.values())
print(user.items())

user2 = user.copy()
# print(user.clear())
print(user2)
# print(user.pop("age"))
print(user.popitem()) #removes last item pair
print(user)
print(user.update({"is_magick" : True}))
print(user)
print(user2)