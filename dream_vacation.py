# 
dream_vacations = {}
dream_active = True

while dream_active:
    name = input("Hello, what's your name? ")
    dream_vacation = input("Where would you like to spend your vacation? ")
    dream_vacations[name] = dream_vacation
    repeat = input("Do you want to  continue the survey or stop the lead (yes/no)? ")
    if repeat == 'no':
        dream_active = False
print("\n--- Results ---")

for name, dream_vacation in dream_vacations.items():
    print(name + " Wants to spend a vacation " + dream_vacation + ".")
