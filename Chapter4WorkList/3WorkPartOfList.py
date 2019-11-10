players = ['charles', 'martina', 'michael', 'florence', 'eli']
# Slicing
print("****** Slicing")
# Gets first 0, 1, and 2 elements inside list
print(players[0:3])
# Specific subset
# prints 1 2 3 element
sub = players[1:4]
print(sub)
# Subset without colon, essentially same as starting at 0
sub = players[:4]
# prints 0 1 2 3 element
print(sub)
# Subset to end of list, 2 3 4 elements
print(players[2:])
# Last 3 players
print(players[-3:])
# Get every even numbered element
print(players[::2])

# Looping through a slice
print("******* Looping through a slice")
print("Here are the first three players on my team:")
# Loop thru subset
for player in players[:3]:
    print(player.title())

# Copying slices and pointer stuffs
print("******* Copying slice")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
#Aliase lists
print("* Aliasing")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
#TLDR: Don't aliase multiple lists, just create copies

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Use a slice to
# print three items from the middle of the list.
# • Print the message The last three items in the list are:. Use a slice to print the
# last three items in the list
print("************** 4-10 **************")
locations = ["Colony 9", "Tephra Cave", "Bionis' Leg", "Colony 6", "Ether Mine", "Satorl Marsh"]
print("The first three items in the list are:")
for loc in locations[:3]:
    print(loc)
# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas .
# Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas .
# • Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the sec-
# ond list. Make sure each new pizza is stored in the appropriate list.
print("************** 4-11 **************")
pizzas = ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon"]
friend_pizzas = pizzas[:]
pizzas.append("Cheese")
friend_pizzas.append("BBQ")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.
print("************** 4-12 **************")
