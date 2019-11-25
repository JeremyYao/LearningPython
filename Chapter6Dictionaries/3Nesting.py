# List of dictionaries
print("**************")
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# List in a dictionary
print("**************")
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
# Iterate through each K-V Pair
for name, languages in favorite_languages.items():
    # Print keys, which is a str
    print(f"\n{name.title()}'s favorite languages are:")
    # Values are list, iterate through them
    for language in languages:
        print(f"\t{language.title()}")

# Dictionary inside a dictionary
print("**************")

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
# Iterate through each K-V pair
for username, user_info in users.items():
    # Username is the key
    print(f"\nUsername: {username}")
    # The value returned is a dictionary, so get those keys
    full_name = f"{user_info['first']} {user_info['last']}"
    # Get value associated with location
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people . Loop through your list of people. As you
# loop through the list, print everything you know about each person.
print("**************6-7")
person = {"firstName": "Jeremy",
          "lastName": "Yao",
          "city": "Columbus"
          }
person1 = {"firstName": "Donald",
           "lastName": "Trump",
           "city": "DC"
           }
person2 = {"firstName": "Michael",
           "lastName": "Jackson",
           "city": "Ded"
           }
persons = [];
persons.append(person)
persons.append(person2)
persons.append(person1)

for currPerson in persons:
    for key, val in currPerson.items():
        print(key.title() + ": " + val.title())
    print()

# 6-8. Pets: Make several dictionaries, where each dictionary represents a differ-
# ent pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets . Next, loop through your list and as
# you do, print everything you know about each pet.
print("**************6-8")
pet1 = {"kind": "fish",
        "owner": "john cena"}
pet2 = {"kind": "dog",
        "owner": "ruby"}
pet3 = {"kind": "dog",
        "owner": "johnathan"}
pets = [pet1, pet2, pet3]

for currPet in pets:
    for key in currPet.keys():
        print(f"{key.title()}: {currPet[key].title()}")

# 6-9. Favorite Places: Make a dictionary called favorite_places . Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.
favorite_places = {'NYC': person, 'Michigan': person1, 'Ohio': person2}
print("**************6-9")
# Loop through key in bigger Dictionary
for place in favorite_places.keys():
    name = ""
    # Loop through keys inside the person
    for item in favorite_places[place].keys():
        # Determine if key has a substring "Name"
        if (item.count("Name") > 0):
            # Get the value from the key
            name = name + favorite_places[place][item] + " "
    print(f"{name}'s favorite place is {place}");

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
# so each person can have more than one favorite number. Then print each per-
# son’s name along with their favorite numbers.
print("**************6-10")
favorite_numbers = {"Bob": [420, 6969],
                    "Pop": [69],
                    "John": [69420, 12341324],
                    "Cena": [420420],
                    "Doug": [0]
                    }

for name, num in favorite_numbers.items():
    print(name + "'s favorite numbers are:")
    for currNum in num:
        print(currNum)
# 6-11. Cities: Make a dictionary called cities . Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country , population , and fact . Print the name of each city and all of the infor-
# mation you have stored about it.
print("**************6-11")
cities = {
    'Akron': {
        'Country': 'USA',
        'Population': 199110,
        'County': 'Summit'
    },
    'Alliance': {
        'Country': 'USA',
        'Population': 22322,
        'County': 'Mahoning'
    },
    'Columbus': {
        'Country': 'USA',
        'Population': 787033,
        'County': 'Franklin'
    }
}

for cityName, cityDict in cities.items():
    print(f"{cityName} has a population of {cityDict['Population']}")
    print(f"{cityName} is located in {cityDict.get('County')} county of the {cityDict.get('Country')}")

# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example pro-
# grams from this chapter, and extend it by adding new keys and values, chang-
# ing the context of the program or improving the formatting of the output.
print("**************6-11")
cities['Cleveland'] = {'Country': 'USA',
                       'Population': 396815,
                       'County': 'Cuyahoga'}

for cityName, cityDict in cities.items():
    print(f"{cityName} has a population of {cityDict['Population']}")
    print(f"{cityName} is located in {cityDict.get('County')} county in Ohio of the {cityDict.get('Country')}")
