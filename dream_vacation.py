# dictionary that holds the results of the poll
poll_result = {}

# a flag variable that either continues or ends the loop
active_poll = True

# while loop that prompts the user for a name and a repsonse
while active_poll:
    name = input('What is your name? ')
    vacation_response = input('Where would you like to travel one day? ')

    # store the user input in the poll dictionary
    poll_result[name] = vacation_response

    # ask the user if they would like to continue the poll
    continue_poll = input('\nWould you like to continue the poll? (yes/no) ')

    # if the user says no change active_poll to False and end the loop
    if continue_poll == 'no':
        active_poll = False

# print out the polling results
print('\n--- Poll Results ---')
for name, response in poll_result.items():
    print(name + ' would like to go to ' + response)