# Define the GeographicEntity class as a base class for Country and City
class GeographicEntity:
    def __init__(self, name: str, population: int, area_km2: float):
        # Initialize common attributes
        self.name = name
        self.population = population
        self.area_km2 = area_km2

    def calculate_population_density(self) -> float:
        # Calculate population density of the geographic entity
        if self.area_km2 > 0:
            return self.population / self.area_km2
        return 0.0

# Define the Country class inheriting from GeographicEntity
class Country(GeographicEntity):
    def __init__(self, name: str, population: int, area_km2: float):
        # Initialize attributes using the parent class constructor
        super().__init__(name, population, area_km2)
        self.cities = []

    def add_city(self, city):
        # Logic to add a city to the country
        if city not in self.cities:
            self.cities.append(city)

    def remove_city(self, city):
        # Logic to remove a city from the country
        if city in self.cities:
            self.cities.remove(city)

# Define the City class inheriting from GeographicEntity
class City(GeographicEntity):
    def __init__(self, name: str, population: int, area_km2: float, is_capital: bool):
        # Initialize attributes using the parent class constructor
        super().__init__(name, population, area_km2)
        self.is_capital = is_capital
        self.landmarks = []

    def add_landmark(self, landmark: str) -> None:
        # Logic to add a landmark to the city
        if landmark not in self.landmarks:
            self.landmarks.append(landmark)

    def update_population(self, new_population: int) -> None:
        # Logic to update the population of the city
        self.population = new_population

    def capital_selection(self) -> None:
        # Logic to handle capital city selection
        self.is_capital = True

    def remove_landmark(self, landmark: str) -> bool:
        # Logic to remove a landmark from the city
        if landmark in self.landmarks:
            self.landmarks.remove(landmark)
            return True
        return False

# Define the Menu class to manage countries
class Menu:
    def __init__(self):
        # Initialize an empty list for countries
        self.countries = []

    def display_options(self):
        # Display the menu options
        pass  # Placeholder statement, the method currently has no implementation

    def select_option(self, option: int):
        # Logic to handle the selected option
        pass

    def show_country(self, country):
        # Logic to show details of a country
        pass

    def remove_country(self, country):
        # Logic to remove a country from the menu
        if country in self.countries:
            self.countries.remove(country)

    def add_country(self, country):
        # Logic to add a new country to the menu
        if country not in self.countries:
            self.countries.append(country)

# Example usage
# Create some cities
berlin = City(name="Berlin", population=3644826, area_km2=891.8, is_capital=True)
frankfurt = City(name="Frankfurt", population=753056, area_km2=248.3, is_capital=False)
paris = City(name="Paris", population=2148327, area_km2=105.4, is_capital=True)
lyon = City(name="Lyon", population=515695, area_km2=47.87, is_capital=False)
rome = City(name="Rome", population=2872800, area_km2=1285, is_capital=True)
milan = City(name="Milan", population=1366180, area_km2=181.8, is_capital=False)

# Add landmarks to Berlin and Frankfurt
berlin.add_landmark("Brandenburg Gate")
berlin.add_landmark("Berlin Wall")
frankfurt.add_landmark("Römer")
frankfurt.add_landmark("Main Tower")

# Create countries and add cities to them
germany = Country(name="Germany", population=83190556, area_km2=357022)
germany.add_city(berlin)
germany.add_city(frankfurt)

france = Country(name="France", population=67081000, area_km2=551695)
france.add_city(paris)
france.add_city(lyon)

italy = Country(name="Italy", population=60317116, area_km2=301340)
italy.add_city(rome)
italy.add_city(milan)

# Calculate population densities
print(f"Population density of {germany.name}: {germany.calculate_population_density():.2f} people per km²")
print(f"Population density of {france.name}: {france.calculate_population_density():.2f} people per km²")
print(f"Population density of {italy.name}: {italy.calculate_population_density():.2f} people per km²")

# Create a menu and add the countries to it
menu = Menu()
menu.add_country(germany)
menu.add_country(france)
menu.add_country(italy)

# Show details of the countries managed by the menu
print(f"Countries managed by the menu: {[country.name for country in menu.countries]}")

# Update the population of Berlin
berlin.update_population(3700000)

# Remove a landmark from Berlin
berlin.remove_landmark("Berlin Wall")

# Show updated details of Berlin
print(f"Updated population of Berlin: {berlin.population}")
print(f"Landmarks in Berlin: {', '.join(berlin.landmarks)}")

# Remove a city from Germany
germany.remove_city(frankfurt)

# Show the updated country details in the menu
menu.show_country(germany)
menu.show_country(france)
menu.show_country(italy)
