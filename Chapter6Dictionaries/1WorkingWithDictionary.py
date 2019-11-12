# Sample dicitonary with 2 key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Empty dictionary
print("***********;Empty Dictionary")
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying Values
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# Deleting stuff
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name , last_name , age , and city . Print each
# piece of information stored in your dictionary.
print("*********** 6-1 ***********")
person = {"firstName": "Jeremy",
          "lastName": "Yao",
          "city": "Columbus"
          }

print(person["city"])
print(person["firstName"])
print(person["lastName"])
# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.
favorite_numbers = {"Bob": 420,
                    "Pop": 69,
                    "John": 69420,
                    "Cena": 420420,
                    "Doug": 0
                    }
num = favorite_numbers["Bob"]
print("Mandy's favorite number is " + str(num) + ".")

num = favorite_numbers['Pop']
print("Micah's favorite number is " + str(num) + ".")

num = favorite_numbers['John']
print("Gus's favorite number is " + str(num) + ".")

num = favorite_numbers['Cena']
print("Hank's favorite number is " + str(num) + ".")

num = favorite_numbers['Doug']
print("Maggie's favorite number is " + str(num) + ".")
# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character ( \n ) to insert a blank line between each word-meaning
# pair in your output.
