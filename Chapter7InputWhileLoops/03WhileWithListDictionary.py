# Start with users that need to be verified,
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing all instances of speicfic values from list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# Filling a Dictionary with User Input
# responses = {}
# # Set a flag to indicate that polling is active.
# polling_active = True
# while polling_active:
#     # Prompt for the person's name and response.
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
#     # Store the response in the dictionary
#     responses[name] = response
#     # Find out if anyone else is going to take the poll.
#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False
#     # Polling is complete. Show the
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")

# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari-
# ous sandwiches. Then make an empty list called finished_sandwiches . Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.
print("****************7-8***************")
sandwich_orders = ["Sandwich1", "Sandwich2", "Sandwich3"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(sandwich + " is ready!")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(sandwich + " was made")
# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders . Make sure no pastrami sandwiches end up
# in finished_sandwiches .
print("****************7-9***************")
sandwich_orders = ["Sandwich1", "pastrami", "pastrami", "pastrami", "Sandwich2", "Sandwich3"]
print("deli has run out of pastrami")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)
# 7-10. Dream Vacation: Write a program that polls users about their dream vaca-
# tion. Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.
print("****************7-10***************")
poll = {}
person = input("Enter your name or nothing to exit: ")
while person != "":
    poll[person] = input("If you could visit one place in the world, where would you go? ")
    person = input("Enter your name or nothing to exit: ")

if poll:
    print("\nHere are the result:")
    for person, place in poll.items():
        print(person + " would like to go to " + place)
else:
    print("Nobody did the poll")
