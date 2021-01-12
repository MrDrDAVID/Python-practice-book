party_size = input('How many people are in your group: ')

party_size = int(party_size)

if party_size >= 8:
    print("I'm sorry your party will have to wait for a table.")
else:
    print('Your table is ready for you now. ')