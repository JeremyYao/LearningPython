
def collatz(number):
    result = None
    if number % 2 == 0:
        result = number / 2
    else:
        result = 3 * number + 1
    return int(result)


keep_running = True
while keep_running:
    try:
        userNum = int(input("Give a positive integer or an invalid input to exit:\n"))
    except ValueError:
        keep_running = False
    else:
        if userNum <= 0:
            print("Number is non-positive")
        while userNum > 1:
            userNum = collatz(userNum)
            print(userNum)


