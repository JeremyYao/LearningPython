# Tuples are immutable lists, where list of items don't change
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Can't assign elements inside tuple new value or change it due to its immutability.
# dimensions[0] = 250

# Tuples are technically defined by the presence of a comma; the parentheses make them
# look neater and more readable. If you want to define a tuple with one element, you
# need to include a trailing comma:
my_t = (3,)

# It doesn’t often make sense to build a tuple with one element, but this can happen
# when tuples are generated automatically

# Loop through Tuple
for dimension in dimensions:
    print(dimension)

# Write over tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# This is just testing stuff, it essentially appends a copy of itself to the end.
dimensions = (400, 100) * 2
print(dimensions)

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the
# change.
# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.
print("********* 4-13 ************")
print("Menu")
foods = ("cheeseburgers", "shish kebab", "ramen", "pizza", "rice")
for food in foods:
    print(food.title())

foods[-1] = "sushi"

print("Menu2")
foods = ("cheeseburgers", "shish kebab", "ramen", "pizza", "sushi", "chicken")
for food in foods:
    print(food.title())