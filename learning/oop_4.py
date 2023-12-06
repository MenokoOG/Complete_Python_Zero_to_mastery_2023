"""OOP lesson L. Jefferson II, Menoko OG, 11/2023"""
class User:
    def __init__(self, email):
        self.email = email
        
    def sign_in(self):
        print("logged in")
    
    

class Wizard(User):
    def __init__(self,  name, power, email):
        super().__init__(email) #running from class above
        self.name = name
        self.power = power
    
    def attack(self):
        print(f"attacking with power of {self.power}")



class Archer(User):
    def __init__(self,  name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f"attacking with arrows: arrows left- {self.num_arrows}")

wizard1 = Wizard("Merlin", 50, "merlin@gmail.com")
archer1 = Archer("Robin", 100)
print(wizard1.email)
print(dir(wizard1)) #introspection-getting a view on methods of object
print("*" * 40)
print(dir(archer1))

