# Displays the entered username
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# 
prompt = "\nTell me something, and I will repear it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# 
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to  end the program. "
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# Compleing a cycle using truth or lies (True, False)
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        acitve = False
    else:
        print(message)