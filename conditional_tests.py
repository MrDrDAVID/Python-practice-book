# All the secret identities of the super heroes
batman_id = 'Bruce Wayne'
superman_id = 'Clark Kent'
flash_id = 'bArRY AlleN'
green_arrow_id = 'oliver queen'

# All the ages of the super heroes
batman_age = 34
superman_age = 34
flash_age = 28
green_arrow_age = 35

# A list of the super heroes secret identities
secret_identites = ['bruce wayne', 'clark kent', 'barry allen', 'oliver queen']

# All the conditional test that will either evaluate to true or false
print("batman_id == 'bruce wayne' will be true")
print(batman_id.lower() == 'bruce wayne')

print("\nclark_id == 'CLARK KENT' will be true")
print(superman_id.upper() == 'CLARK KENT')

print("\nflash_id == 'Barry Allen' will be false")
print(flash_id == 'Barry Allen')

print("\ngreen_arrow_id == 'olive queen' will be false")
print(green_arrow_id == 'olive queen')

print("\nsuperman_id != batman_id will be true")
print(superman_id != batman_id)

print("\nbatman_age == superman_age will be true")
print(batman_age == superman_age)

print("\nbatman_age != superman_age will be false")
print(batman_age != superman_age)

print("\nflash_age < green_arrow_age will be true")
print(flash_age < green_arrow_age)

print("\nbruce wayne is in the list")
print('bruce wayne' in secret_identites)

print("\nDick Grason is not in the list")
print("Dick Grayson" not in secret_identites)

print("\nClark Kent is not in the list")
print('clark kent' not in secret_identites)