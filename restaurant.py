class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        ''''''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def desctibe_restaurant(self):
        ''''''
        print("Restautrant name " + self.restaurant_name.title())
    
    def open_restaurant(self):
        ''''''
        print("Restautrant " + self.restaurant_name.title())
    
    def served_number(self):
        ''''''
        print("Served " + str(self.number_served))

    def set_number_sevred(self, person):
        ''''''
        self.number_served = person
    
    def increment_number_served(self, persons):
        self.number_served += persons

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

    def iceream(self):
        print("Ice cream stand")

    def flavors(self):
        ice = ['fruit icecream', 'berry ice cream']
        print("Name ice:" + str(ice))



my_restaurant = Restaurant('restaurant', 8)
your_restaurant = Restaurant('bob stile', 11)
one_restaurant = Restaurant('firts by', 6)
print("Name restaurant " + my_restaurant.restaurant_name.title())
print("Open restaurant " + str(my_restaurant.cuisine_type))
print("Name restaurant " + your_restaurant.restaurant_name.title())
print("Open restaurant " + str(your_restaurant.cuisine_type))
print("Name restaurant " + one_restaurant.restaurant_name.title())
print("Open restaurant " + str(one_restaurant.cuisine_type))
# my_restaurant.number_served = 2
# my_restaurant.served_number()

my_restaurant.set_number_sevred(5)
my_restaurant.served_number()

my_restaurant.increment_number_served(2)
my_restaurant.served_number()

my_icecreamstand = IceCreamStand('fruit', 'berry ice cream')
my_icecreamstand.iceream()
my_icecreamstand.flavors()