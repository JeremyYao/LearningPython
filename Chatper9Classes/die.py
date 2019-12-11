import random

# 9-13. Dice: Make a class Die with one attribute called sides , which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll it
# 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

class Die:

    def __init__(self, num_sides = 6):
        self.num_sides = num_sides

    def roll_die(self):
        print(random.randint(1, self.num_sides))

# Make a 6-sided die and roll it
# # 10 times.
# # Make a 10-sided die and a 20-sided die. Roll each die 10 times.
sixDie = Die()
for i in range(0, 10):
    sixDie.roll_die()

print("******** tenDie **********8")
tenDie = Die(10)
for i in range(0, 10):
    tenDie.roll_die()

print("******** twentyDie **********8")
twentyDie = Die(20)
for i in range(0, 10):
    twentyDie.roll_die()
