from random import randint

x = randint(1, 6)
print(x)

class Die():
    def roll_die(self, sides=6):
        self.sides = sides
        sides = randint(1, self.sides)
        print(self.sides)

cubes = Die()
print(cubes.roll_die(sides=10))
print(cubes.roll_die(sides=10))
print(cubes.roll_die(sides=20))