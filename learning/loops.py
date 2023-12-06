"""Loop stuff, L. Jefferson II, Menoko OG, 11-2023"""
for item in (1,2,3,4,5):
    for x in ["a", "b", "c",]:
        print(item, x)
print("*" * 40)
#dictionary iterating
user = {
    "name": "golem",
    "age": 5006,
    "can_swim": False
}
for item in user.items(): #returns tuple object
    print(item)
for key, value in user.items():
    print(key, value) #prints out
for item in user.values():
    print(item)
for item in user.keys():
    print(item)
print("*" * 40)

#range
for number in range (0, 10, 2):
    print(number)
for _ in range (10, 0, -1):
    print(_)
for _ in range(2):
    print(list(range(10)))
print("*" * 40)
#enumerate, a good way for indexing items
for i, char in enumerate("hello"):
    print(i, char)
#print just index of number 50 from range
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f"index of 50 is: {i}")
print("*" * 40)
#while  loop
i = 0
while i < 50:
    print(i)
    i += 1
    # break
else:
    print("done with all the work")
print("*" * 40)
my_list = [1,2,3]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# hi and bye
while True:
    response = input("say something: ")
    if response == "bye":
        break
print("*" * 40)