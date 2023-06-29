

# Class
class Monster:

    ### Dunder method
    def __init__ (self,health,energy,name):
        self.health = health
        self.energy = energy
        self.name = name
    
    def __len__(self):
        return len(self.name)
    
    def __abs__(self):
        return 7

    def __call__(self):
        print("This is call dunder method")

    def __add__(self,add):
        return self.health + add

    def __str__(self):
        return f"Name: {self.name}\nEnergy: {self.energy}\nHealth: {self.health}"
    ### method
    def info(self):
        print(f"Health: {self.health}")
        print(f"Energy: {self.energy}")

    def attack(self):
        self.health -=20
        print("Monster is attacking")
        print(f"Health: {self.health}")

    def move(self,speed):
        print(f"Monster moving with {speed} speed")


# object

monster = Monster(energy=50,health=25,name="Monster")
monster1 = Monster(100,50,"Raju")

print(monster)
print(monster1)