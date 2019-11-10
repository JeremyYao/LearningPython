# Generic lists
listNum = [1, 2, 3, 4, 5]
strList = ["Bob", "The", "BUilDer", "yes"]

# Indexing
print((strList[0] + " "+ strList[2]).title())
# Print last element in listNum
print(listNum[-1])
# Second to last ad third to last
print(listNum[-2])
print(strList[-3])
#Printing
print(f"I am {listNum[-1]} years old\n")

# 3-1. Names: Store the names of a few of your friends in a list called names . Print
# each person’s name by accessing each element in the list, one at a time.
# and 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each mes-
# sage should be the same, but each message should be personalized with the
# person’s name.
names = ["Me" ,"Myself", "And" ,"I"]
for temp in names:
    print("Hello " + temp)
#
# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”
names = ["Ford GT", "Dodge Demon", "Bugatti", "Tesla", "Lamborghini"]
for temp in names:
    print("I would love to ride a " + temp)
