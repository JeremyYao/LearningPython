import json


# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dump() to store this number in a file. Write a separate pro-
# gram that reads in this value and prints the message, “I know your favorite
# number! It’s _____.”
# 10-12. Favorite Number Remembered: Combine the two programs from
# Exercise 10-11 into one file. If the number is already stored, report the favorite
# number to the user. If not, prompt for the user’s favorite number and store it in a
# file. Run the program twice to see that it works.
def prompt_write_favorite_number(file_name):
    fav_nums = []
    message = "Give a valid number or Q to quit: "
    response = input(message)
    while not response.upper().__eq__("Q"):
        try:
            fav_nums.append(float(response))
        except ValueError:
            print("Uh oh, the number wasn't valid!")
        response = input(message)

    file = open(file_name, 'w')
    json.dump(fav_nums, file)
    file.close()

def read_json_favorite_number(file_name):
    file = open(file_name, 'r')
    fav_nums = json.load(file)
    file.close()
    print("Here are your favorite numbers:")
    print(fav_nums)

# def does_file_exist(file_name):
#     result = True
#     try:
#         file = open(file_name)
#     except FileNotFoundError:
#         result = False
#     else:
#         file.close()
#
#     return result


# file_name = "favorite_number.json"
file_name = input("Give name of json file to be written to or read: ")
while not file_name.__eq__(""):
    try:
        tempFile = open(file_name)
    except:
        print("File doesn't exist, creating new file")
        prompt_write_favorite_number(file_name)
    else:
        tempFile.close()
        print(f"{file_name} exists!")
        temp_response = input("Type y to re-write it or anything else for it to be read")
        if temp_response.lower().__eq__('y'):
            prompt_write_favorite_number(file_name)
        else:
            read_json_favorite_number(file_name)
    file_name = input("Give name of json file to be written to or read: ")

print("Program stopping")
