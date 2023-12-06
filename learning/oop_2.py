"""OOP lesson L. Jefferson II, Menoko OG, 11/2023"""
#how to make variables private
class PlayerCharacter:
    def __init__(self, name, age):
        # self.name = name 
        # self.age = age
        self._name = name #the underscore lets other programmers know that these attributes should not be altered. as there is no real private variable in python.
        self._age = age
        
    def run(self):
        print("run")
        return "done"
    
    def speak(self):
        print(f"my name is {self._name} and I am {self._age} years old")
    
player1 = PlayerCharacter("Voltron", 300)
print(player1.speak())