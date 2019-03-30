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
