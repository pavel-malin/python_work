responses = {}

# Set the flag to continue the survey.
polling_active = True

while polling_active:
    # Request name and user response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # The answer is stored in the dictionary.
    responses[name] = response

    # Check the continuation of the survey.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# The survey is completed, display the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")