my_pizzas = ["pepperoni", "deep dish", "meat extravaganza", "cheese", "Hawaiian"]

boos_pizzas = my_pizzas[:]

print('My favorite pizzas are: ')
print(my_pizzas)

print('\nYour favorite pizzas are: ')
print(boos_pizzas)

my_pizzas.append('Supreme')
boos_pizzas.append('Philly Cheese')

print('\nMy favorite pizzas are: ')
for pizzas in my_pizzas:
    print(pizzas)

print('\nBoos favorite pizzas are: ')
for pizzas in boos_pizzas:
    print(pizzas)