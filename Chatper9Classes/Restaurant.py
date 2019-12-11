# 9-1. Restaurant: Make a class called Restaurant . The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type .
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.

# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any num-
# ber you like that could represent how many customers were served in, say, a
# day of business.

class Restaurant:
    def __init__(self, restaurant_name="", cuisine_type="", number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print("Restaurant Name: " + str(self.restaurant_name.title()))
        print("Cuisine Type: " + str(self.cuisine_type.lower()))

    def open_restaurant(self):
        print("Resturant is open")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, incr):
        self.number_served += incr


# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand , and call this method

class IceCreamStand(Restaurant):

    def __init__(self, name, flavors = []):
        super().__init__(restaurant_name=name, cuisine_type="Ice Cream")
        self.flavors = flavors

    def printFlavors(self):
        for flavor in self.flavors:
            print(flavor)

    def setFlavors(self, flavors):
        self.flavors = flavors

mcdonalds = Restaurant("McDonalds", "Fast food")
print(mcdonalds.restaurant_name)
print(mcdonalds.cuisine_type)
mcdonalds.describe_restaurant()
mcdonalds.open_restaurant()
# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

bk = Restaurant("Burger King", "Fast food")
bk.describe_restaurant()
redLobster = Restaurant("Red Lobster", "seafood")
redLobster.describe_restaurant()
reddit = Restaurant("reddit", "memes")
reddit.describe_restaurant()

print("********* 9-4 **********")
print(reddit.number_served)
reddit.set_number_served(69420)
print(reddit.number_served)
reddit.number_served = 1
print(reddit.number_served)
reddit.increment_number_served(420)
print(reddit.number_served)

print("********* 9-6 **********")
jenis = IceCreamStand("Jeni's", ['Vanilla', 'Chocolate'])
jenis.printFlavors()
jenis.describe_restaurant()