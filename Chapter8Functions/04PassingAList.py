# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages() , which prints each text message.
print("*********8-9*********")
initMessages = ["And", "His", "Name", "Was"]


def show_messages(messages):
    for message in messages:
        print(message)


show_messages(initMessages)
# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.
print("*********8-10*********")
sentMessages = []


def send_messages(messages, storedList):
    show_messages(messages)
    # Create a copy of messages (Not a copy of the reference value but the obj inside it)
    while messages:
        storedList.append(messages.pop())


send_messages(initMessages, sentMessages)
print(initMessages)
print(sentMessages)

# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained its
# messages.
print("*********8-11*********")
send_messages(sentMessages, initMessages)
print(initMessages)
print(sentMessages)
