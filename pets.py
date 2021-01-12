jalapena = {
    'Breed': 'IDK',
    'Owner': 'Laineyboo'
}

puppy = {
    'Breed': 'Beagle',
    'Owner': 'Laineysboo'
}

meat_head = {
    'Breed': 'Pitbull',
    'Owner': 'Elaine'
}

piper = {
    'Breed': 'German Shepard',
    'Owner': 'Boo'
}

pets = [jalapena, puppy, meat_head, piper]

for pet in pets:
    print(pet['Owner'] + "'s dog is a " + pet['Breed'])