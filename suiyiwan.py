from random import randint

class Die():
    def __init__(self,x):
        self.x = x
    def roll_die(self):
        print(str(self.x))

for side in range(10):
    x = randint(1,10)
    my_die = Die(x)
    my_die.roll_die()
