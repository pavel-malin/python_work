# Displays the price of the ticket throught the
# cycle by age of the buyer
ticket_price = "\nEnter your age for cinema ticket price."
ticket_price += "\nTo complete the operation see 'quit': "
ticket = input(ticket_price)

while True:
    age = int(ticket)
    if age <= 12:
        print("\tTo pay: $10")
        ticket = input(ticket_price)
        if ticket == 'quit':
            print("\tGoodbye!!!")
            break
    else:
        print("\tTo pay: $15")
        ticket = input(ticket_price)
        if ticket == 'quit':
            print("\tGoodbye!!!")
            break
