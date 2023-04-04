# 9-10
# 9-1
class Restaurant:
    """
    An extremely simplified version of a restaurant.
    """
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

        # 9-4
        self.number_served = 0

    def describe_restaurant(self):
        """
        Provides a brief description of the restaurant.
        """
        print(f"\nRestaurant name: {self.restaurant_name}")
        print(f"Restaurant type: {self.cuisine_type}")

    def open_restaurant(self):
        """
        Prints a message saying the restaurant is open.
        """
        print(f"{self.restaurant_name} is now open for business!")

    # 9-4
    def set_number_served(self, served):
        """
        Sets the number of people served to a certain value.
        """
        self.number_served = served

    def increment_number_served(self, served):
        """
        Increments the number of people served by a certain value.
        """
        self.number_served += served

# 9-6
class IceCreamStand(Restaurant):
    """
    An ice cream stand that has flavors!
    """
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry", "Oreo"]

    def display_flavors(self):
        """
        Prints the names of all flavors of ice cream for the store.
        """
        print(f"{self.restaurant_name} has the following ice cream flavors:")
        for flavor in self.flavors:
            print(f"-- {flavor}")