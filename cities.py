city = {
    'Paramount' : {
        'country' : 'USA',
        'population' : 54000,
        'fact' : 'David Garza lives in paramount.',
    },

    'Melbourne' : {
        'country' : 'Austrailia',
        'population' : 4000000,
        'fact' : 'Melbourne is in the southeastern part of mainland Australia, within the state of Victoria.',
    },

    'Aberdeen' : {
        'country' : 'United Kingdom',
        'population' : 212000,
        'fact' : 'That it has the lowest unemployment rate in Scotland.',
    },
}

for cities, cityInfo in city.items():
    print('\n' + cities + ':')
    print('\tIs a city located in ' + cityInfo['country']+ ' and has a population of ' + str(cityInfo['population']))
    print('\tA fact about ' + cities + ' is: ' + '\n\t' + cityInfo['fact'])