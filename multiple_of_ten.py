num = input('Give me any number and I wll be able to tell you if it is ' +
            'a multiple of ten or not: ')

num = int(num)

if num % 10 == 0:
    print('The number you entered is a multiple of ten')
else:
    print('The number you entered is not a multiple of ten')