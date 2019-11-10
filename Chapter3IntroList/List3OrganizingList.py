# Reverse using sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
# Alphabetical order
cars.sort()
print(cars)
# Another sort using reverse alphabetical order
cars.sort(reverse=True)
print(cars)

# Sorted()- sort temporarily
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
# Not explained in book:
# sorted(list) returns a value
sortedCars = sorted(cars)
print(sortedCars)
print("\nHere is the original list again:")
print(cars)
print()

# Printing list in reverse order
print(cars)
cars.reverse()  # Reverses the actual array itself and updates itself
print(cars)

# Getting length of list
l = len(cars)
print(l)

print("********* Practice problems **********")
# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse alphabetical order without chang-
# ing the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.
print("********* 3-8 **********")
locations = ["Colony 9", "Tephra Cave", "Bionis' Leg", "Colony 6", "Ether Mine", "Satorl Marsh"]
print(locations)
print(sorted(locations))
print(locations)
sortedLoc = sorted(locations)
sortedLoc.sort(reverse=True)
print(sortedLoc)
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)
# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 42), use len() to print a message indicating the number
# of people you are inviting to dinner.
print("********* 3-9 **********")
guestList = ["Terry", "Plant", "Joker", "Hero", "Banjo", "Kazooie"]

print(f"{len(guestList)} is the number of people invited to smash")
# 3-10. Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or any-
# thing else you’d like. Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.
print("********* 3-10 **********")
