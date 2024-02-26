class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name +" (Level" +  str( self.level) + ")")

name = input("Enter player's name:\n")
level = input("Enter player's level:\n")

player = Player(name, level)
player.intro()