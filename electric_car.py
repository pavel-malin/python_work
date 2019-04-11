class Car():
    '''Simple car model.'''
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_desctiptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    '''Simple electric car battery model.'''
    def __init__(self, battery_size=70):
        '''Initializes battery attributes.'''
        self.battery_size = battery_size
    def describe_battery(self):
        '''Displays battery capacity information.'''
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
    def get_range(self):
        '''Displays the estimated power reserve for the battery.'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElecticCar(Car):
    '''Represents aspects of the car that are special for electic vehicles.
    It then initializes attributes specific to the elechtic vehicle.'''
    def __init__(self, make, model, year):
        '''Intializes the attributes of the parent class.'''
        super().__init__(make, model, year)
        # self.battery_size = 70
        self.battery = Battery()
    
    # def describe_battery(self):
        # '''Displays battery power information.'''
        # print("This car has a " + str(self.battery_size) + "-kwh battery.")
     
    def fill_gas_tank(self):
        '''Electric vehicles do not have a gas tank.'''
        print("This car doen't need a gas tank!")

my_tesla = ElecticCar('tesla', 'model s', 2016)
print(my_tesla.get_desctiptive_name())
# my_tesla.describe_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()