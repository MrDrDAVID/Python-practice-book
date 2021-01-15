'''Returns the given city and country, neatly formatted'''
def city_country(city, country):
    formatted_city_coutry = city + ', ' + country
    return formatted_city_coutry.title() 

city_and_country = city_country('paramount', 'california')

print(city_and_country)