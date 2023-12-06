"""Generator lesson, L. Jefferson II, Menoko OG, 11/2023"""
#interable
#iterate- taking something, doing something to it and going to next one
#generators are iterable, but not everything iterable is a generator, generator is sbset of iterable.

def generator_function(num):
    for i in range(num):
        yield i * 2 #pauses function and then come back to it once the next keyword is called as seen below example

g = generator_function(100)
next(g) #next can be called up until the interation object is exhausted the raises stopinteration error.
next(g)
print(next(g))
        
# for item in generator_function(100): #this deos not create 100 things in memory as the function below would.
#     print(item)       
        
# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result

# my_list = make_list(100)
# print(my_list)