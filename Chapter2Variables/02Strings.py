# Chapter 2: Variables
print("Hello World!")

# 2-2 :Assign a message to a variable, and print that message.
# Then change the value of the variable to a new message, and print the new
# message.
message = "bob"
print(message)
message = "ross"

# String method stuff
last = "ross";
first = "bob"
# f-Strings, format strings puts obj values inside of string
fullname  = f"{first} {last}"
# title is a string method
print(fullname.title());
print(f"Hello, {fullname.title()}!")

# Tabs and newlines
message = "\tBob\n\tRoss\n"
print(message)
message = "        BobRoss           "
# Returns new string obj with trailing spaces removed from right or left
print(message.rstrip())
print(message.lstrip())
#Stip string entirely of trailing spaces
message = message.rstrip();
message = message.lstrip();
print(message)

# 2-7. Stripping Names: Use a variable to represent a person’s name, and include
# some whitespace characters at the beginning and end of the name. Make sure
# you use each character combination, "\t" and "\n" , at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip() ,
# rstrip() , and strip() .

name = "\t\t\t\n\n\njeremy yao\n\n\n\n\n    \t"
#Stips trailing whitespace from r and l. Then title-cases string.
print(name.strip().title());