class Monster:

    def __init__(self,health,energy):
        self.health = health
        self.energy = energy

    def attack(self,amount):
        print("The monster is attack")
        print(f"{amount} damage is delt")

    def move(self,speed):
        print("The monter has moved")
        print(f"It has a speed of {speed}")

class Camel(Monster):
    def __init__(self,speed,health,energy):
        # Monster.__init__(self,health,energy)
        super().__init__(health,energy)
        self.speed = speed
    
    def get_water(self):
        print("The camel is drinking water")

    def move(self):
        print("The camel is travelling")
        print(f"It's speed is {self.speed}")

class Scorpion(Monster):
    def __init__(self,poision,health,energy):
        super().__init__(health,energy)
        self.poision = poision

    def attack(self):
        print("The scorion is attack")
        print(f"{self.poision} damage is delt")


### Creating camel object

scorpion = Scorpion(25,50,100)
scorpion.attack()

