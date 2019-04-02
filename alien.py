# Dictionary creation and dictionary output
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# Dictionary change
alien_0 = {'color': 'green'}

print(alien_0['color'])

# Output a specific word category
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']

print("You just earned " + str(new_points) + " points!")

# Regular dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
# Adding output by coordinaes
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Adding to empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Change vocabulary and result
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# Change and check for increase
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# The alien moves to the right
# Calculate offser based on current speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # The alien moves fast
    x_increment = 3
# The new position is equal to the sum of the position and
# increment
alien_0['x_posiion'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# Deletion from the dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# 
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Creating an empty list for
# storing aliens
aliens = []
# Create 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Conclusion of the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Displays the number of created alien
print("Total number of aliens: " + str(len(aliens)))

# Creating an empty list for
# storing aliens
aliens = []
# Create 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Conclusion of the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# 
# Creating an empty list for
# storing aliens
aliens = []
# Create 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Conclusion of the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Simplify code using  dictionary to display information
aliens = {
    'alien_0': {
        'color': 'green',
        'points': 5,
        },
    'alien_1': {
        'color': 'yellow',
        'points': 10,
        },
    'alien_2': {
        'color': 'red',
        'points': 15,
        },
    }

for alien, info in aliens.items():
    print("\nAll info: " + alien)
    color = info['color']
    points = info['points']
    if color == 'green':
        print("\tColor: " + color.title())
        print("\tPoints: " + str(points))
    elif color == 'yellow':
        print("\tColor: " + color.title())
        print("\tPoints: " + str(points))
    elif color == 'red':
        print("\tColor: " + color.title())
        print("\tPoints: " + str(points))


