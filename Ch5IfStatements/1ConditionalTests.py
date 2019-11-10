# Simple example
print("*********** Simple example")
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Ignore case when checking.
print("*********** Ignore case when checking.")
car = 'Audi'
print(car.lower() == 'audi')

# Inequality
print("*********** Inequality")
print(car.upper() != 'audi')
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Numerical equality and comparison
# TLDR != == > >= <= <=

# Using ors and ands

# Checking if value in list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print("*********** Check value in list")
# Both are false
print('mushrooms          ' in requested_topping)
print('pepperoni' in requested_toppings)

# Checking if value not in list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print("*********** Check value not in list")
# Both are True
print('mushrooms          ' not in requested_topping)
print('pepperoni' not in requested_toppings)

# Boolean expressions
print("********Boolean expressions")
isActive = True
isActive = False
# Some experimenting with not Keyword
print(not isActive)
print(not not isActive)

# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False .
# • Create at least ten tests. Have at least five tests evaluate to True and
# another five tests evaluate to False .
print("**************** 5-1 *******************")
sexuality = 'gay'
print("am I gay'? I predict True.")
print(sexuality == 'gay')
print("checking with \"gay\"")
print(sexuality == "gay")

print("am I homo? I predict false.")
print(sexuality == 'homo')
# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to ten. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list
print("**************** 5-2 *******************")
locations = ["Colony 9", "Tephra Cave", "Bionis' Leg", "Colony 6", "Ether Mine", "Satorl Marsh"]
print(locations[0].upper() == "COLONY 9")
print(locations[0] == "ColonY 9")
print(locations[0].lower() == "colony 9")
print(69 >= 420)

print("Is Mechonis field in locations?")
print(("Mechonis field").title() in locations)
print("Is Satorl Marsh in locations?")
print(("Satorl Marsh") in locations)
# Random tests of for loops, ignore pls
locations = [loc.upper() for loc in locations]
print(locations)
# Prints out locations with all uppercase, pretty cool! Book didn't talk about it :(
