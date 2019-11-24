user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
# SImple for loop to loop through k-v pairs
# .items() returns a list of kv pairs
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Loops trought all keys
for name in favorite_languages.keys():
    print(name.title())
# for name in favorite_languages: also exhibits same behavior as above
for name in favorite_languages:
    print(name.title())

# Print it out sorted
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
# Print out all values
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
# Print out all values without duplicates by converting list to set
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
# Declaring and creating set variables
languages = {'python', 'ruby', 'python', 'c'}

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt' .
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary
print("******************6-5***************8")
Rivers = {'Nile': 'Egypt',
          'Amazon': 'Brazil',
          'Ganges': 'China'}
for name, loc in Rivers.items():
    print(f"{name} is in {loc}")
