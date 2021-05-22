from random import randint
class Die:

	def __init__(self, sides=6):
		self.sides=sides

	def roll_die(self):
		a = randint(1,self.sides)
		print(f"Die landed on {a}")

my_die = Die(100)
for i in range(10):
	my_die.roll_die()