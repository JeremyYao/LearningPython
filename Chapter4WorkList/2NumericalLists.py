# range() function
# only prints 1 - 4 inclusive
for value in range(1, 5):
    print(value)

# only prints 0 - 69 inclusive
for value in range(70):
    print(value)

# Transorms range to list
numbers = list(range(79))
print(numbers)
# Even numbers
# Prints even numbers from 2 to 10 inclusive
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#Create list of squares using range()
squares = []
for value in range(1, 11):
    #square individual value
    square = value ** 2
    #Add to end of list
    squares.append(square)

print(squares)

#Min max sum
print(min(squares))
print(max(squares))
print(sum(squares))

# List of squares using list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.
print("************** 4-3 **************")
for i in range(21):
    print(i)
# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl -C or by closing the output window.)
print("************** 4-4 **************")
numList = [value for value in range(10**6 + 1)]
for i in numList:
    print(i)

# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.
print("************** 4-5 **************")
print(f"Min {min(numList)}")
print(f"Max {max(numList)}")
print(f"Sum {sum(numList)}")

# 4-6. Odd Numbers: Use the third argument of the range() function to make a
# list of the odd numbers from 1 to 20. Use a for loop to print each number.
print("************** 4-6 **************")
oddNums = []
for value in range(1, 20, 2):
    print(value)
    oddNums.append(value)

print(oddNums)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
print("************** 4-7 **************")
mult3 = list(range(3, 31, 3))

for value in mult3:
    print(value)
# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.
print("************** 4-8 **************")
cubes = [value**3 for value in range(1,11)]
for value in cubes:
    print(value)
# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.
print("************** 4-9 **************")
cubes = [value**3 for value in range(1,11)]
