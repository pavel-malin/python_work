class Dog:
    '''Simple dog model.'''

    def __init__(self, name, age):
        '''Initializes the name and age attributes.'''
        self.name = name
        self.age = age

    def sit(self):
        '''Dog to sit the team.'''
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        '''The dog rolls on command.'''
        print(self.name.title() + " rolled over")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".") 
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()