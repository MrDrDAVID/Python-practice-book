# This lets you write a name to a file
with open('guest_name.txt', 'w') as file_object :
    guest_name = input('What is your name? ')
    file_object.write(guest_name)

# This lets you check in multiple people and writes them all to a file
with open('guest_book.txt', 'w') as file_object :
    while True :
        name = input('What is your name? (or enter quit to end.)')

        if name == 'quit' :
            break

        print('Hello ' + name + ' welcome. ')

        file_object.write(name + ' has checked in. \n')

# This takes in a poll of many different reasons why people like programming and writes them to a file
with open('programming_poll.txt', 'a') as file_object :
    while True :
        poll_reason = input('Why do you like programming? (or enter exit)')

        if poll_reason == 'exit' :
            break

        file_object.write(poll_reason + '\n')