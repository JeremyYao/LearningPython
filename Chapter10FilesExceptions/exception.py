# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int , you’ll get a ValueError . Write a program that prompts for
# two numbers. Add them together and print the result. Catch the ValueError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number.

# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number

print("This program adds two numbers the user gives")
cont_response = input("Continue? Y/N: ")
nums = []
TOTALNUM = 2
while cont_response.upper().__eq__("Y"):
    i = 0
    while i < TOTALNUM:
        try:
            nums.append(float(input(f"Number {i}:")))
        except:
            print("That number wasn't a number, try again")
        else:
            i += 1

    print("The sum is " + str(sum(nums)))
    cont_response = input("Continue? Y/N")
