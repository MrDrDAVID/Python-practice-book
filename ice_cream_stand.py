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

class IceCreamStand(Restaurant) :
    """
    Represent aspects of a restaurant, more specific to an ice cream stand
    """
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self) :
        print('Ice cream flavors available: ')
        for flavor in self.flavors :
            print(' -' + flavor)
            
ice_cream_flavors = ['vanilla', 'chocolate', 'strawberry', 'cookies n cream'] 

ice_cream_stand = IceCreamStand('Boos Frozen Treats', 'Ice Cream')
ice_cream_stand.flavors = ice_cream_flavors
ice_cream_stand.display_flavors()
