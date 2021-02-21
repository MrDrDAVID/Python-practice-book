def format_city_country(city, country, population='') :
    '''Takes in a city and a country and returns properly formatted city, country string'''

    if population :
        formatted_city_country = city + ', ' + country + ' - population ' + population
    else :
        formatted_city_country = city + ', ' + country
    

    return formatted_city_country.title()