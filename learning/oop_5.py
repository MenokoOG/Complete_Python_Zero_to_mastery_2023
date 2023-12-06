"""OOP lesson L. Jefferson II, Menoko OG, 11/2023"""
class User:
        
    def sign_in(self):
        print("logged in")
    
    

class Wizard(User):
    def __init__(self,  name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f"attacking with power of {self.power}")



class Archer(User):
    def __init__(self,  name, arrows):
        self.name = name
        self.arrows = arrows
    
    # def attack(self):
    #     print(f"attacking with arrows: arrows left- {self.num_arrows}")
    
    def check_arrows(self):
        print(f"{self.arrows} remaining")
    
    def run(self):
        print("ran really fast")

class HybridBorg(Wizard, Archer): #multiple inheritance
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1 = HybridBorg("borgy", 50, 100)
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())