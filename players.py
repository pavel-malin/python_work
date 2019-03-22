# Slices 1-4
players = ['charles', 'martina', 'machael', 'florence', 'eli']
print(players[0:3])

# Slices 2-4
players = ['charles', 'martina', 'machael', 'florence', 'eli']
print(players[1:4])

# Slices 1-4
players = ['charles', 'matrina', 'machael', 'florence', 'eli']
print(players[:4])

# Slices 3-5
players = ['charles', 'matrina', 'machael', 'florence', 'eli']
print(players[2:])

# Slices 3-5
players = ['charles', 'matrina', 'machael', 'florence', 'eli']
print(players[-3:])

#bust
players = ['charles', 'matrina', 'florence', 'machael', 'eli']
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())