class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Cat object with 3 cats
starbuck = Cat("Starbuck", 301)
skywalker = Cat("Skywalker", 205)
jonsnow = Cat("JonSnow", 1001)


# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)


# Output
print(f"The oldest cat is {get_oldest_cat(starbuck.age, skywalker.age, jonsnow.age)} years old.")