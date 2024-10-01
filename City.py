class City:
    # Class attributes based on our UML diagram with default values
    city_name: str = "unnamed"
    population: int = 0
    is_capital: bool = False
    area_km2: float = 0.0
    # We use a set with the assumption that we don't have two landmarks with the same name.
    # If that assumption is incorrect, we can use a list instead, like this: landmarks: list = []
    landmarks: set = set()
    
    # This section defines our attributes using the constructor method.
    def __init__(self, city_name: str = "unnamed", population: int = 0, is_capital: bool = False, area_km2: float = 0.0) -> None:
        # We use 'self' as a reference to the instance of the class.
        self.city_name = city_name
        self.population = population
        self.is_capital = is_capital
        self.area_km2 = area_km2
        self.landmarks = set()

    """ 
    The @property decorator allows us to access population_density as if it were a regular attribute. 
    Some benefits include readability and encapsulation. Without it, the code can't be run correctly without error.
    """
    @property
    def population_density(self) -> float:
        if self.area_km2 == 0:
            # Prevent division by zero error
            return 0.0
        return self.population / self.area_km2

    # Here, we use the previous property and make it a method.
    def calculate_population_density(self) -> float:
        return self.population_density

    # A method to add a landmark to our set, which is empty by default.
    def add_landmark(self, landmark: str) -> None:
        self.landmarks.add(landmark)

    # If the population changes over time, we can simply update it with this method.
    def update_population(self, new_population: int) -> None:
        self.population = new_population

    # The city is by default not a capital, but this method can change it to a capital city, like Berlin.
    def capital_selection(self) -> None:
        self.is_capital = True

    # Since we can add landmarks, we also need a method to remove them.
    def remove_landmark(self, landmark: str) -> bool:
        # Check if the landmark exists for the ability to remove it.
        if landmark in self.landmarks:
            self.landmarks.remove(landmark)
            print("The landmark was removed from the set.")
            return True
        print("The chosen landmark was not in the set.")
        return False

    # This method will show all attributes of the City class to the user.
    def show_info(self) -> None:
        print(f"\nCity Info:")
        print(f"City Name: {self.city_name}")
        print(f"Population: {self.population}")
        print(f"Is Capital: {self.is_capital}")
        print(f"Area (km²): {self.area_km2}")
        print(f"Population Density: {self.calculate_population_density()}")
        """ 
        In this line, we use the join method to create a string from the landmark set,
        separated by ", ". If the set is empty, 'None' will be displayed by default.
        """
        print(f"Landmarks: {', '.join(self.landmarks) if self.landmarks else 'None'}")












"""

# Use real data to create instances of the City class 

# Berlin
berlin = City("Berlin", 3645000, True, 891.8)
berlin.add_landmark("Brandenburg Gate")
berlin.add_landmark("Berlin Wall")
berlin.add_landmark("Reichstag Building")

# Hamburg
hamburg = City("Hamburg", 1841000, False, 755.2)
hamburg.add_landmark("Elbphilharmonie")
hamburg.add_landmark("Miniatur Wunderland")
hamburg.add_landmark("St. Michael's Church")

# Munich
munich = City("Munich", 1472000, False, 310.7)
munich.add_landmark("Marienplatz")
munich.add_landmark("English Garden")
munich.add_landmark("Nymphenburg Palace")

# Cologne
cologne = City("Cologne", 1086000, False, 405.2)
cologne.add_landmark("Cologne Cathedral")
cologne.add_landmark("Museum Ludwig")
cologne.add_landmark("Hohenzollern Bridge")

# Frankfurt
frankfurt = City("Frankfurt", 753000, False, 248.3)
frankfurt.add_landmark("Römer")
frankfurt.add_landmark("Main Tower")
frankfurt.add_landmark("Palmengarten")

# Show information for each city
berlin.show_info()
hamburg.show_info()
munich.show_info()
cologne.show_info()
frankfurt.show_info()

"""