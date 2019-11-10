#Test pointers w/ numbers
i = 1
j = 3
j = i
i = 33;
print(i)
print(j)
#Result: no aliasing
#j is 1 and i is 33
#They appear to be immutable or when assigned, make copies

#Test pointesr w/ floating points
i = 1.1
j = 3.1
j = i
i = 33.1;
print(i)
print(j)
#Same result as 1st test