class Restaurant() :
    """
    A restaurant class that holds the attributes name and cuisine type
    and methods that describe the restaurant and display when its open
    """
    def __init__(self, restaurant_name, cuisine_type) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def restaurant_description(self) :
        print('The name of this restaurant is ' + self.restaurant_name +
        ' and it serves ' + self.cuisine_type)

    def open_for_business(self) :
        print(self.restaurant_name + ' is open for business')

    def increment_number_served(self) : 
        self.number_served += 100
        print(f'We served {self.number_served} guests today')

    def set_number_served(self, num_served) :
        self.number_served = num_served
        

new_restaurant = Restaurant("Boo's diner", 'boos butt')

print(new_restaurant.number_served)

new_restaurant.number_served = 50

print(new_restaurant.number_served)

new_restaurant.increment_number_served()

new_restaurant.set_number_served(2000)
print(new_restaurant.number_served)