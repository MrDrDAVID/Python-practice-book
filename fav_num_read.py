import json

file_name = 'text-files/fav_num.json'

with open(file_name) as file_obj :
    fav_num = json.load(file_obj)
    print('I remebered your favorite number. Its ' + fav_num)