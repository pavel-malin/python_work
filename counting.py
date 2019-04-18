# Output from 1 to 5 using a loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Loop output using odd digits and repeating 
# the loop until 10
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# Output from 1 to 5 using a loop
x = 1
while x <= 5:
    print(x)
    x += 1