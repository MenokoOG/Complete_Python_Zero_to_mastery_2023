"""Generator lesson, L. Jefferson II, Menoko OG, 11/2023"""
def specail_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            # print(next(iterator))
            print(next(iterator) * 2)
            
        except StopIteration:
            break

specail_for([1,2,3]) #the objects occupy same memory space.
print("*" * 40)
#our own range function, how under the hood for Range function.
class myGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if myGen.current < self.last:
            num = myGen.current
            myGen.current += 1
            return num
        raise StopIteration

gen = myGen(0,100)
for i in gen:
    print(i)
