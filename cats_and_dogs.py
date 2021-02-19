def cats_and_dogs_file() :
    '''Reads in names of cats and dogs from file'''
    dogs_file = 'text-files\dogs.txt'
    cats_file = 'text-files\cats.txt'
        
    try :
        with open(dogs_file) as dog_file :
            print(dog_file.read())

        with open(cats_file) as cat_file :
            print(cat_file.read())
        
        with open('rat.txt') as rats_file :
            print(rats_file.read())

    except FileNotFoundError :
        #print('The file does not exist. ')
        pass

cats_and_dogs_file()