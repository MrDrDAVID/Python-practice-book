class Restaurant() :
    """
    A restaurant class that holds the attributes name and cuisine type
    and methods that describe the restaurant and display when its open
    """
    def __init__(self, restaurant_name, cuisine_type) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def restaurant_description(self) :
        print('The name of this restaurant is ' + self.restaurant_name +
        ' and it serves ' + self.cuisine_type)

    def open_for_business(self) :
        print(self.restaurant_name + ' is open for business')

new_restaurant = Restaurant("Boo's diner", 'boos butt')

print(new_restaurant.restaurant_name)
print(new_restaurant.cuisine_type)
new_restaurant.restaurant_description()
new_restaurant.open_for_business()