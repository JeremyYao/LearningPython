# Example of using args to make tuple with mutliple args
def make_pizza(size, *toppings):
    # """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Multiple keyword-value args example
def build_profile(first, last, **user_info):
    # Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the sand-
# wich that’s being ordered. Call the function three times, using a different num-
# ber of arguments each time.
print("*********8-12*********")


def sandwichSummary(*items):
    print("The sandwich will have the following:")
    for item in items:
        print(item)


sandwichSummary("Ranch", "Bread", "Meat")
sandwichSummary("Ranch")
sandwichSummary("ASDASd", "ASDASDADS", "QWIHEIUQWHDI", "ASDSADASD", "Your mom")


# 8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a
# profile of yourself by calling build_profile() , using your first and last names
# and three other key-value pairs that describe you.


# 8-14. Cars: Write a function that stores information about a car in a diction-
# ary. The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. Call the func-
# tion with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.
print("*********8-14*********")
def make_car(manufacturer, model, **features):
    features["manufacturer"] = manufacturer
    features["model"] = model
    return features


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
