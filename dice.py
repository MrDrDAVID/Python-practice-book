from random import randint

class Die() :
    """Representation of a die"""
    def __init__(self, sides=6) :
        self.sides = sides

    def roll_die(self) :
        print('The number ' + str(randint(1, self.sides)) + ' has been rolled.')

new_die = Die()

new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()
new_die.roll_die()

super_new_die = Die(10)
super_new_die.roll_die()
super_new_die.roll_die()
super_new_die.roll_die()
super_new_die.roll_die()
super_new_die.roll_die()
super_new_die.roll_die()
super_new_die.roll_die()
