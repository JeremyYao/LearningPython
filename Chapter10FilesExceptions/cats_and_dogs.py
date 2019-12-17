# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
# names of cats in the first file and three names of dogs in the second file. Write
# a program that tries to read these files and print the contents of the file to the
# screen. Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a file is missing. Move one of the files to a dif-
# ferent location on your system, and make sure the code in the except block
# executes properly.
try:
    catFile = open('cats.txt')
    dogFile = open('dogs.txt')
    # Commented out as this could also be put into the else block
    # I think that you normally don't include the below lines as it helps show what
    # Exception you're trying to find and what lines may cause the exception
    # catStr = catFile.read().rstrip()
    # dogStr = dogFile.read().rstrip()
    # print(catStr)
    # print(dogStr)
except FileNotFoundError:
    print("At least one of the files doesn't exist!")
else:
    catStr = catFile.read().rstrip()
    dogStr = dogFile.read().rstrip()
    print(catStr)
    print(dogStr)
    catFile.close()
    dogFile.close()
