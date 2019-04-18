cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)


def make_cars(models, outback, color, **info_cars):
    '''Information about the car'''
    car_info = {}
    car_info['models'] = models
    car_info['color'] = color
    for key, value in car_info.items():
        car_info[key] = value
    return car_info

info_cars = make_cars('bmw', 'ger', 'red', tow_package=True)
print(info_cars)