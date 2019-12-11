# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the
# values that are returned.
print("*********8-6*********")


def city_country(cityName, countryName):
    return cityName + ", " + countryName


print(city_country("New York", "New York"))
print(city_country("Dublin", "Ohio"))
print(city_country("Assgard", "MCU"))

# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.
print("*********8-7*********")


def make_albums(artistName, albumTitle, numSongs=None):
    album = {"Artist": artistName,
             "Title": albumTitle}
    if numSongs:
        album["# of Songs"] = numSongs
    return album


print(make_albums("Mike", "Ross", 69420))
print(make_albums("Bob", "Ross"))
# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.
print("*********8-8*********")
artistName = "1"
while artistName != "":
    artistName = input("Give an artist name or nothing to quit:")
    if artistName != "":
        albumTitle = input("Give name of album:")
        print(make_albums(artistName, albumTitle))
