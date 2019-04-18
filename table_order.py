# Asking guests their number
table_order = input("How many people do you need a table? ")
number = int(table_order)

if number > 8:
    print("Sorry, but we don't have  table for so many people, please wait.")
else:
    print("We have a table for your company in quantity: " + str(number))