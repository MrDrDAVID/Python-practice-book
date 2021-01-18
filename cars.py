def car_info(model, manufacturer, **other_car_info):
    car_details = {}

    car_details['model'] = model
    car_details['manufacturer'] = manufacturer

    for key, value in other_car_info.items():
        car_details[key] = value
    
    return car_details

car = car_info('accord', 'honda', color='black', type='four door', insured=True)
print(car)