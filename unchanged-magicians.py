magician_names = ['David Blaine', 'Cris Angel', 'Houdini', 'Harry Potter', 'Wutan']

def great_magicians(magicians):
    '''Function that modifies the string in a list'''
    magicians[:] = ['The Great ' + magician for magician in magicians]
    return magicians

def show_magicians(magicians):
    '''Function that prints out all the elements in a list'''
    for magician in magicians:
        print('Please welcome to the stage ' + magician)

print('The orginal magicians list: ')
show_magicians(magician_names)

print('\nThe modified copy of magician names: ')
great_mags = great_magicians(magician_names[:])
show_magicians(great_mags)

print('\nThe original list one more time to prove that it wasnt modified: ')
show_magicians(magician_names)