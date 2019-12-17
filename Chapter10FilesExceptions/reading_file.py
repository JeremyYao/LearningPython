# 10-1. Learning Python: Open a blank file in your text editor and write a few
# lines summarizing what you’ve learned about Python so far. Start each line
# with the phrase In Python you can. . . . Save the file as learning_python.txt in
# the same directory as your exercises from this chapter. Write a program that
# reads the file and prints what you wrote three times. Print the contents once by
# reading in the entire file, once by looping over the file object, and once by stor-
# ing the lines in a list and then working with them outside the with block.

#Text contains the full text of the file
print("***********")
file = open('scratch.txt', 'r')
text = file.read().rstrip() + "\n"
print(text)
#Note to self: If end of file is reached, read will return ""
#Using seek brings you to a certain line, use seek(0) to bring you back to top of file.
file.seek(0)

#Loop through file obj
print("***********")
text = ""
for line in file:
    text += line.rstrip() + "\n"
print(text)
file.seek(0)

#Store lines in a list
print("***********")
text = ""
lines = file.readlines()
for line in lines:
    text += line.rstrip() + "\n"

print(text)
print("***********")
# 10-2. Learning C: You can use the replace() method to replace any word in a
# string with a different word. Here’s a quick example showing how to replace
# 'dog' with 'cat' in a sentence:
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# Read in each line from the file you just created, learning_python.txt, and
# replace the word Python with the name of another language, such as C. Print
# each modified line to the screen.
print(text.replace("Python", "Java"))
file.close()