def make_sammiches(*ingredients):
    '''Prints out all the ingredients being put into the sandwich'''
    for ingredient in ingredients:
        print(ingredient + ' is being added to the sandwich.')
    print('')

make_sammiches('lettuce', 'tomatoes', 'bacon')
make_sammiches('chicken', 'cheese')
make_sammiches('ham', 'cheese', 'mayo', 'pickles', 'lettuce')