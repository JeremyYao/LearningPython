# Keyword argumented funciton example
def describe_pet(animal_type, pet_name):
    # """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='hamster', pet_name='harry')


# Setting default values for paramets without any argument given
def describe_pet1(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet1(pet_name='willie')

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.
print("*********8-3*********")


def shirt(size, message):
    print(f"The {size} shirt says: {message}")


shirt("XL", "AKJSDLASKJD")
shirt(message="Hello", size="S")
# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.
print("*********8-5*********")


def shirt(size="L", message="I love Python"):
    print(f"The {size} shirt says: {message}")


shirt()
shirt("M")
shirt(message="I watched RWBY lol")
# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland . Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.
print("*********8-6*********")


def describe_city(cityName="Columbus", country="USA"):
    print(cityName + " is in " + country)


describe_city("Reykjavik", "Iceland")
describe_city("New York")
describe_city()
