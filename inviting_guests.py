# Guest invitation exetcise
guest = ['Ang', 'Favi', 'Doni', 'Po']

# Offsets
message_ang = "Hello, " + guest[0].title() + " invite you to dinner"
message_favi = "Hello, " + guest[1].title() + " invite you to dinner"
message_doni = "Hello, " + guest[2].title() + " invite you to dinner"
message_po = "Hello, " + guest[3].title() + " invite you to dinner"
print(message_ang)
print(message_favi)
print(message_doni)
print(message_po)
print(len(guest))

# Can't come
print("\n" + guest[2].title() + " can not come\n")

# Guest replacement
guest[2] = 'Ada'
message_ada = "Hello, " + guest[2].title() + " invite you to dinner"

# New list guest
print(message_ada)
print(message_ang)
print(message_favi)
print(message_po)
print("\n!!!!NOTIFICATION!!!!\n", "Add Guest")

# Add guest list 
guest.append('Mul')
guest.append('Peri')
guest.append('Emi')
guest.append('Bi')

# New offsets
message_mul = "Hello, " + guest[4].title() + " invite you to dinner"
message_peri = "Hello, " + guest[5].title() + " invite you to dinner"
message_emi = "Hello, " + guest[6].title() + " invite you to dinner"
message_bi = "Hello, " + guest[7].title() + " invite you to dinner"

# New guest list
print("\n" + message_ada)
print(message_ang)
print(message_bi)
print(message_emi)
print(message_peri)
print(message_po)
print(message_favi)
print(message_mul)
print(len(guest))

# Add guest list
guest.insert(0, 'Dodi')
guest.insert(5, 'Popi')
guest.append('Mydak')

message_dodi = "Hello, " + guest[0].title() + " invite you to dinner"
message_ang = "Hello, " + guest[1].title() + " invite you to dinner"
message_favi = "Hello, " + guest[2].title() + " invite you to dinner"
message_ada = "Hello, " + guest[3].title() + " invite you to dinner"
message_po = "Hello, " + guest[4].title() + " invite you to dinner"
message_popi = "Hello, " + guest[5].title() + " invite you to dinner"
message_mul = "Hello, " + guest[6].title() + " invite you to dinner"
message_peri = "Hello, " + guest[7].title() + " invite you to dinner"
message_emi = "Hello, " + guest[8].title() + " invite you to dinner"
message_bi =  "Hello, " + guest[9].title() + " invite you to dinner"
message_mydak = "Hello, " + guest[10].title() + " invite you to dinner"

# New guest list
print("\n" + message_dodi)
print(message_ang)
print(message_favi)
print(message_ada)
print(message_po)
print(message_popi)
print(message_mul)
print(message_peri)
print(message_emi)
print(message_bi)
print(message_mydak)
print(len(guest))

# Notice that only I can come for lunch two
print("\nSorry, " + guest[0] + " for dinner only two guests can get there")
print("Sorry, " + guest[1] + " for dinner only two guests can get there")
print("Sorry, " + guest[2] + " for dinner only two guests can get there")
print("Sorry, " + guest[3] + " for dinner only two guests can get there")
print("Sorry, " + guest[4] + " for dinner only two guests can get there")
print("Sorry, " + guest[5] + " for dinner only two guests can get there")
print("Sorry, " + guest[6] + " for dinner only two guests can get there")
print("Sorry, " + guest[7] + " for dinner only two guests can get there")
print("Sorry, " + guest[8] + " for dinner only two guests can get there")
print("Sorry, " + guest[9] + " for dinner only two guests can get there")
print("Sorry, " + guest[10] + " for dinner only two guests can get there")

# Delete list guests (two gues)
print("\nSorry " + guest.pop(0) + " about canceling the invitation")
print("Sorry " + guest.pop(2) + " about canceling the invitation")
print("Sorry " + guest.pop(3) + " about canceling the invitation")
print("Sorry " + guest.pop(4) + " about canceling the invitation")
print("Sorry " + guest.pop(5) + " about canceling the invitation")
print("Sorry " + guest.pop(-6) + " about canceling the invitation")
print("Sorry " + guest.pop(-5) + " about canceling the invitation")
print("Sorry " + guest.pop(-4) + " about canceling the invitation")
print("Sorry " + guest.pop(-3) + " about canceling the invitation")
print(len(guest))

# The inviation is valid
print("\nHello " + guest[0] + ", the lunch offer remains valid")
print("Hello " + guest[1] + ", the lunch offer remains valid")
print(len(guest))

# Clear guests list
del guest
guest = []
print(guest)

