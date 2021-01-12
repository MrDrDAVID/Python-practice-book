sandwich_orders = ['BLT', 'Philly cheesesteak', 'Ham & cheese', 'Veggie', 'Chicken', 'Meatball', 'Tuna']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print('Your ' + current_sandwich.title() + ' sandwich is ready.')

    finished_sandwiches.append(current_sandwich)

print('\nThe following sandwiches are ready for pickup: ')
for sandwich in finished_sandwiches:
    print(sandwich)