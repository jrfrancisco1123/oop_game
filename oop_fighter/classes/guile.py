class Guile:
    def __init__(self, name):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self

    def normal_attack(self, bison):
        if self.health > 0:
            bison.health -= 5
            self.speed += 1
            print(f"{self.name}\nHP: {self.health}\nSpeed: {self.speed}")
        else:
            print("Need to charge up!")
        return self

    def sonic_boom(self, bison):
        if self.speed >= 2 and self.health > 0:
            bison.health -= (self.strength + 5)
            self.speed -= 1
            print(f"{self.name}\nHP: {self.health}\nSpeed: {self.speed}")
        else:
            print("Need to charge up!")
        return self
    
    def flash_kick(self, bison):
        if self.speed >= 3 and self.health > 0:
            bison.health -= (self.strength + 10)
            self.speed -= 2
            print(f"{self.name}\nHP: {self.health}\nSpeed: {self.speed}")
        else:
            print("Need to charge up!")
        return self
    
    def sonic_hurricane(self, bison):
        if self.health <= 35 and self.speed >= 3 and self.health > 0:
            bison.health -= (self.strength + 20)
            self.speed -= 3
            print(f"{self.name}\nHP: {self.health}\nSpeed: {self.speed}")
        else:
            print("Ultra is not ready")
        return self