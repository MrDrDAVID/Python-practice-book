def addition_calculator() :
    '''Take in two numbers and adds them together'''
    while True :
        try :
            num1 = input('Enter a number: (or enter quit)')
            if num1 == 'quit' :
                break

            int1 = int(num1)

            num2 = input('Enter another number to add: (or enter quit)')
            if num2 == 'quit' :
                break
            
            int2 = int(num2)

        except ValueError :
            print('You must enter an number value.')

        else :
            sum = int1 + int2

            print(sum)
    
addition_calculator()