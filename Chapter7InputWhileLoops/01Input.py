# # How input() works
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
#
# # Prompts longer than 1 line
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")
#
# # Using int() to accept numerical input
# height = input("How tall are you, in inches? ")
# # int()parses the str
# height = int(height)
# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”
print("****************7-1***************")
car = input("What kind of car would you like? ")

print("Let me see if I can find you a " + car)
# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message say-
# ing they’ll have to wait for a table. Otherwise, report that their table is ready.
print("****************7-2***************")
numPeople = int(input("how many people are in your dinner group? "))

ans = "You'll have to wait"
if (numPeople <= 8):
    ans = "Your table is ready"

print(ans)

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.
print("****************7-3***************")
num = int(input("Give a number: "))

ans = str(num) + " is not a multiple of 10"
if num % 10 == 0:
    ans = str(num) + " is a multiple of 10"

print(ans)
