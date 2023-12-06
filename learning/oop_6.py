"""OOP lesson L. Jefferson II, Menoko OG, 11/2023"""
#MRO - Method Resolution Order
class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1
    

class D(B, C):
    pass

print(D.mro())
print(D.num)