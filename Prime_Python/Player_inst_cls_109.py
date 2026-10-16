class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

p1 = Player("Amit", 5)
p2 = Player("Rahul", 3)
p3 = Player("Sneha", 7)

print("Total players : ", Player.player_count)
