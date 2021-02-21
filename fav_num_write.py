import json

file_name = 'text-files/fav_num.json'

with open(file_name, 'w') as file_object :
    fav_num = input('What is your favorite number? ')
    json.dump(fav_num, file_object)

    print('Your favorite number is ' + fav_num)