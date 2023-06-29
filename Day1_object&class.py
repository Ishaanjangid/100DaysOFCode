# This is me restarting the journey


# This is Class (BluePrint)
class Entity:
    ### attribute == variable
    ### method == function

    # attribute
    health = 50
    energy = 90
    speed = 30
    
    # __dunder__ method

    def __init__ (self,health,energy) :

        self.health = health
        self.energy = energy

    
    # methods
    def attack(self):
        print("The player is attacking")
        print(f"{self.health} health") #self.health == player_joe.health
        
    def move(self,speed):
        print(f"Player moves with {speed}")
        


# Creating object

kartik = Entity(100,50)

print(kartik.health)
print(kartik.energy)