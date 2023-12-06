"""OOP lesson, L. Jefferson II, Menoko OG, 11/2023"""
class PlayerCharacter: #note: naming is singular becasue this is blueprint for objects.
    membership = True #class object attribute, can not modify in objects, all objects have htis attribute.
    def __init__(self, name, age):
        if (PlayerCharacter.membership): #making sure has membership before contstructing object. in this case it is becasue class attribute is set to true
            self.name = name #attribute
            self.age = age
        
    def run(self):
        print("run")
        return "done"
    
    def shout(self):
        print(f"my name is {self.name}")
    
    @classmethod #can be called even if no objects created from class, class method
    # def adding_things(cls, num1, num2): 
    #     return num1 + num2
    def adding_things(cls, num1, num2): 
        return cls("Johan", num1 + num2) #now an object can be created
    
    @staticmethod # no access to class or cls as class mehtod
    def adding_things2(num1, num2):
        return num1 +num2

# player1 = PlayerCharacter("LJ", 51)
# player2 = PlayerCharacter("joJo", 23)
# player2.attack = 50
player3 = PlayerCharacter.adding_things(7,3)

# print(player1.name) #calling attribute
# print(player2.name)
# print(player1.age)
# print(player2.age)
# print(player1) #shows where in memory
# print(player2)
# print(player2.attack) #calling object attribute, separate from class
# print(player1.run()) #calling method from class
# print(player2.run())
# print(player1.membership)
# print(player1.shout())
# print(player2.shout())
print(PlayerCharacter.adding_things2(4,5)) #static method call
print(player3.age)