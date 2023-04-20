class Bison:
    def __init__(self, name):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self
    
    def normal_attack(self, guile):
        if self.health > 0:
            guile.health -= 5
            self.speed += 1
            print(f"{self.name}\nHP: {self.health}\nSpeed: {self.speed}")
        return self
    
    def psycho_crusher (self, guile):
        if self.speed >= 4 and self.health > 0:
            guile.health -= (self.strength + 10)
            self.speed -= 2
            print(f"{self.name}\nHP: {self.health}\nSpeed: {self.speed}")
        else:
            print("Need to charge up!")
        return self
    
    def scissor_kick(self, guile):
        if self.speed >= 3 and self.health > 0:
            guile.health -= (self.strength + 5)
            self.speed -= 2
            print(f"{self.name}\nHP: {self.health}\nSpeed: {self.speed}")
        else:
            print("Need to charge up!")
        return self
    
    def ultimate_pyscho_crusher(self, guile):
        if self.health <= 30 and self.speed >= 3 and self.health > 0:
            guile.health -= (self.strength + 20)
            self.speed -= 3
            print(f"{self.name}\nHP: {self.health}\nSpeed: {self.speed}")
        else:
            print("Ultra is not ready")
        return self


