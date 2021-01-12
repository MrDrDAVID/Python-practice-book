sandwich_orders = ['pastrami', 'BLT', 'Philly cheesesteak', 'pastrami',  'Ham & cheese', 'Veggie', 'pastrami', 'Chicken', 'Meatball', 'Tuna']

print("I'm sorry but we have run out of pastrami today. \n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print('Your ' + current_sandwich.title() + ' sandwich is ready.')

    finished_sandwiches.append(current_sandwich)

print('\nThe following sandwiches are ready for pickup: ')
for sandwich in finished_sandwiches:
    print(sandwich)