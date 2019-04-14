'''Class to represent the car.'''
class Car:
    '''Simple car model.'''
    def __init__(self, make, model, year):
        '''Initializes the vehicle description attributes.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Returns an accurate formatted description.'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        '''Displays the mileage of the car in miles.'''
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
       # '''Sets the mileage of the odometer.'''
       # self.odometer_reading = mileage
        '''Sets the mileage of the odometer.
        At attempt of the return twisting change is rejected.'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        '''Increases odometer reading with a given increment.'''
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()