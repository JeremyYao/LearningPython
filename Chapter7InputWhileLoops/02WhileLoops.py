# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.
print("****************7-4***************")
userInput = ""
while userInput != 'quit':
    userInput = input("enter a series of pizza toppings or quit to exit:")
# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.
print("****************7-5***************")
userInput = input("Give age as integer or nothing to exit: ")
while userInput != "":
    userAge = int(userInput)
    ans = "Ticket is $10"

    if userAge > 12:
        ans = "Ticket is $15"
    elif userAge < 3:
        ans = "Ticket is free"
    print(ans)
    userInput = input("Give age or nothing to exit: ")

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.
# I already did the first one, the other two complicates it and the last one makes bad habits in programming

# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
# ctrl -C or close the window displaying the output.)
print("****************7-7***************")
while True:
    print("LOL WHY DID U RUN THIS XD")