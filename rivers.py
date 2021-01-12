major_rivers = {
    'Mississippi River': 'The United States',
    'Zambezi River': 'Africa',
    'Nile River': 'Egypt',
}

for river, country in major_rivers.items():
    print('The ' + river +
        ' runs through ' + country)

for river in major_rivers.keys():
    print('\n' + river)

for country in major_rivers.values():
    print('\n' + country)