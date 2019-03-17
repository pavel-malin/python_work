# All functions (upper, lower, title, del, pop, remove, reverse, 
# sort, sorted, len, \n, \t, add, append, strip, lstrip, rstrip)

# Count list
list_world = ['USA', 'Russai', 'Belarus', 'Poland', 'Litva', 'Latvia',
            'Americ', 'Ukraina', 'Yaponia', 'China', 'Africa', 'Canada']

# Alphabe order list
list_world.sort()
print(list_world)

# Length list
print(len(list_world))

list_world.sort(reverse=True)
print(list_world)

list_world.reverse()
print(list_world)

kirkoi = 'Ukraina'
list_world.remove(kirkoi)
print(list_world)

list_world.pop(5)
print(list_world)

list_world.append('Latvia')
print(list_world)

# Animals list
list_animals = ['dog', 'cat', 'tiger', 'lion', 'lizard', 'toad',
                'elephant', 'hyena', 'wolf', 'rhino']

# Alphabe order list
list_animals.sort()
print(list_animals)

# Length list
print(len(list_animals))

print("\nLife " + list_world[3].title() + " animal " + list_animals[6].title())