buffet_items = ('pizza', 'chicken', 'meatloaf', 'cheesecake', 'french fries')

print('The restaurant offers these food: ')

for foods in buffet_items:
    print(foods)

# tuples are not allowed to be modified so this doesnt work
#buffet_items[0] = 'rice'

buffet_items = ('pizza', 'chicken', 'turkey', 'cherry pie', 'french fries')

print('\nWe recently changed two items from the menu. ')
print('Here is the new menu: ')

for food in buffet_items:
    print(food)