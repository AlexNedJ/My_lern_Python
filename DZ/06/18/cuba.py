import random as r

class Die():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
         print(r.randint(1, self.sides))
my_cub = Die()
my_cub.roll_die()
my_cub.roll_die()
my_cub.roll_die()
my_cub.roll_die()
my_cub.roll_die()
my_cub.roll_die()
