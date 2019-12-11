import random


# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and
# five letters. Randomly select four numbers or letters from the list and print a
# message saying that any ticket matching these four numbers or letters wins a
# prize.

def generate_rand_ticket():
    lottery_list = []
    # Generate 10 random ints in interval [0,10]
    for i in range(10):
        lottery_list.append(str(random.randint(0, 10)))

    # Generate 5 capital letters
    for i in range(5):
        charAdd = chr(random.randint(65, 89))
        lottery_list.append(charAdd)

    winList = []
    # Choose 4 random items in lotteryList to be the winning list without replacement
    for i in range(4):
        winList.append(lottery_list.pop(random.randint(0, lottery_list.__len__() - 1)))

    print("Any ticket matching these four numbers or letters wins a prize.")
    print(winList)
    return winList


# Do lists contain the same elements given they are both the same size? Note that ordering doesn't matter
def has_same_elements(l1=[], l2=[]):
    is_same = l1.__len__() == l2.__len__()
    #Create copies of the list
    l1Copy = l1[:]
    l2Copy = l2[:]

#Pop first item in L2 and check if it's in l1
    item = l2Copy.pop(0)
    is_same = item in l1Copy
    while l2Copy.__len__() > 0 and is_same:
        #Remove the item from L1 so that it can't be checked twice
        l1Copy.remove(item)
        item = l2Copy.pop(0)
        is_same = item in l1Copy

    return is_same


# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
# the kind of lottery you just modeled. Make a list or tuple called my_ticket .
# Write a loop that keeps pulling numbers until your ticket wins. Print a message
# reporting how many times the loop had to run to give you a winning ticket.

#list containing all iterations where two tickets have same elements.
index_matches = []
#Perform 10 test cases
for i in range(0, 10):
    myTicket = ['0', '1', 'O', 'L']
    numTickets = 0
    #Repeatly check if user ticket and random one contain same elements
    while (not has_same_elements(myTicket, generate_rand_ticket())):
        numTickets += 1
        print("Currently on ticket " + str(numTickets))
        #Add the iteration they match into list containing when they match
    index_matches.append(numTickets)

print(index_matches)
#Sample run: [14490, 3888, 47542, 87180, 52010, 25219, 50523, 22453, 11053, 216103]