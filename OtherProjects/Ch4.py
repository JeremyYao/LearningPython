def print_grammatically_corrected(list):
    list_size = len(list)
    if list_size == 1:
        print(list[0])
    else:
        list_item = list.pop(0)
        print(f"{list_item}, ", end='')
        if len(list) == 1:
            print("and ", end='')
        print_grammatically_corrected(list)

def print_2D_grid(grid):
    str = ""
    for row in grid:
        for curr_char in row:
            str += curr_char
        str += "\n"

    print(str)


#Proplem statement
# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam list to
# the function would return 'apples, bananas, tofu, and cats' . But your func-
# tion should be able to work with any list value passed to it.
spam = ['apples', 'bananas', 'tofu', 'cats', 'asdfasdf', 'asdf343dsxfg']
print_grammatically_corrected(spam)

grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]
print_2D_grid(grid)