# Conclusion, names of magicians
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# Cunclusion, names of magicians with appeal. With thanks
magician = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.
        title() + ".\n")


print("Thank you, everyone. That was a great magic show!")

# Cunclusion, names of magicians with appeal.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick," + magician.title() + 
    ".\n")\

# Thanks to every magician
magician = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

    print("Thank you everyone, that was a great magic show!")

# 
def show_magicians(names):
    for name in names:
        print("I can't wait to see your next trick, " + name.title() + ".\n")

magician = ['alice', 'david', 'carolina']
show_magicians(magician)

def show_1magicians(magicians, copy_magicians):
    while magicians:
        current_magicians = magicians.pop()
        print("Magicians: " + current_magicians.title())
        copy_magicians.append(current_magicians)

def show_magicians_copy(copy_magicians):
    print("\nCopy magicians: ")
    for copy_magician in copy_magicians:
        print(copy_magician.title() + ' Great')

magicians = ['alice', 'david', 'carolina']
copy_magicians = []
show_1magicians(magicians, copy_magicians)
show_magicians_copy(copy_magicians)

def show_0magicians(magicians, copy_magicians):
    while magicians:
        current_magicians = magicians.pop()
        print("Magicians: " + current_magicians.title())
        copy_magicians.append(current_magicians)

def show_magicians_0copy(copy_magicians):
    print("\nCopy magicians: ")
    for copy_magician in copy_magicians:
        print(copy_magician.title() + ' Great')
        magician_show = magicians[:]
    for magician_show in magicians:
        bachup_magician = "Bachup copy:\t" + magician_show.title()   
        print(bachup_magician)

magicians = ['alice', 'david', 'carolina']
copy_magicians = []
show_0magicians(magicians[:], copy_magicians)
show_magicians_0copy(copy_magicians)
