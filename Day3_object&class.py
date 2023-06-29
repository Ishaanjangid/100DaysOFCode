class Monster:
    def __init__(self,func):
        self.func = func

class Attack:

    def bite(self):
        print("Bite")

    def strike(self):
        print("Strike")

    def slash(self):
        print("slash")

    def kick(self):
        print("Kick")



monster = Monster(Attack().bite())