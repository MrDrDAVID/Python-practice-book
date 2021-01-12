alien1_color = 'green'
alien2_color = 'red'
alien3_color = 'yellow'

# Part 1
# if alien1_color == 'green':
#     print('The player just earned 5 points')

# Part 2
# if alien1_color == 'green':
#     print('The player shot down a green alien and earned 5 points')
# else:
#     print('The player earned 10 points')

# if alien2_color == 'green':
#     print('The player shot down a green alien and earned 5 points')
# else:
#     print('The player earned 10 points')

# Part 3
if alien1_color == 'green':
    print('The player shot down a ' + alien1_color + ' alien and earned 5 points')
elif alien1_color == 'yellow':
    print('The player shot down a ' + alien1_color + ' alien and earned 10 points')
else:
    print('The player shot down a ' + alien1_color + ' alien and earned 15 points')

if alien2_color == 'green':
    print('\nThe player shot down a ' + alien2_color + ' alien and earned 5 points')
elif alien2_color == 'yellow':
    print('\nThe player shot down a ' + alien2_color + ' alien and earned 10 points')
else:
    print('\nThe player shot down a ' + alien2_color + ' alien and earned 15 points')

if alien3_color == 'green':
    print('\nThe player shot down a ' + alien3_color + ' alien and earned 5 points')
elif alien3_color == 'yellow':
    print('\nThe player shot down a ' + alien3_color + ' alien and earned 10 points')
else:
    print('\nThe player shot down a ' + alien3_color + ' alien and earned 15 points')