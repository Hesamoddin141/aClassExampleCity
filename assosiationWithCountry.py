# making the Menu class
class Menu:
    def __init__(self):
        # define The constructor method with a initialize empety list for countries
        self.countries = []

    def display_options(self):
        # Display the menu options 
        pass
        # A placeholder statement, the method currently has no implementation

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

# making the Country class with some methods
class Country:
    def __init__(self, country_name: str, population: int, area_km2: float):
        self.country_name = country_name
        self.population = population
        self.area_km2 = area_km2
        self.cities = []

    def add_city(self, city):
        # Logic to add a city to the country
        if city not in self.cities:
            self.cities.append(city)

    def remove_city(self, city):
        # Logic to remove a city from the country
        if city in self.cities:
            self.cities.remove(city)

    def calculate_population_density(self) -> float:
        # Calculate population density of the country
        if self.area_km2 > 0:
            return self.population / self.area_km2
        return 0.0

# Using our exist City class
class City:
    def __init__(self, city_name: str, population: int, is_capital: bool, area_km2: float):
        self.city_name = city_name
        self.population = population
        self.is_capital = is_capital
        self.area_km2 = area_km2
        self.landmarks = []

    def calculate_population_density(self) -> float:
        # Calculate population density of the city
        if self.area_km2 > 0:
            return self.population / self.area_km2
        return 0.0

    def add_landmark(self, landmark: str):
        # Logic to add a landmark to the city
        if landmark not in self.landmarks:
            self.landmarks.append(landmark)

    def update_population(self, new_population: int):
        # Logic to update the population of the city
        self.population = new_population

    def capital_selection(self):
        # Logic to handle capital city selection as defalt false value 
        self.is_capital = False

    def remove_landmark(self, landmark: str) -> bool:
        # Logic to remove a landmark from the city
        if landmark in self.landmarks:
            self.landmarks.remove(landmark)
            return True
        return False
    




"""                     Example usage of the Menu, Country, and City classes                          """


# Create some cities
berlin = City(city_name="Berlin", population=3644826, is_capital=True, area_km2=891.8)
frankfurt = City(city_name="Frankfurt", population=753056, is_capital=False, area_km2=248.3)

paris = City(city_name="Paris", population=2148327, is_capital=True, area_km2=105.4)
lyon = City(city_name="Lyon", population=515695, is_capital=False, area_km2=47.87)

rome = City(city_name="Rome", population=2872800, is_capital=True, area_km2=1285)
milan = City(city_name="Milan", population=1366180, is_capital=False, area_km2=181.8)

# Add landmarks to Berlin and Frankfurt
berlin.add_landmark("Brandenburg Gate")
berlin.add_landmark("Berlin Wall")

frankfurt.add_landmark("Römer")
frankfurt.add_landmark("Main Tower")

# Create countries and add cities to them
germany = Country(country_name="Germany", population=83190556, area_km2=357022)
germany.add_city(berlin)
germany.add_city(frankfurt)

france = Country(country_name="France", population=67081000, area_km2=551695)
france.add_city(paris)
france.add_city(lyon)

italy = Country(country_name="Italy", population=60317116, area_km2=301340)
italy.add_city(rome)
italy.add_city(milan)

# Calculate population densities
print(f"Population density of {germany.country_name}: {germany.calculate_population_density():.2f} people per km²")
print(f"Population density of {france.country_name}: {france.calculate_population_density():.2f} people per km²")
print(f"Population density of {italy.country_name}: {italy.calculate_population_density():.2f} people per km²")

# Create a menu and add the countries to it
menu = Menu()
menu.add_country(germany)
menu.add_country(france)
menu.add_country(italy)

# Show details of the countries managed by the menu
print(f"Countries managed by the menu: {[country.country_name for country in menu.countries]}")

# Update the population of Berlin
berlin.update_population(3700000)

# Remove a landmark from Berlin
berlin.remove_landmark("Berlin Wall")

# Show updated details of Berlin
print(f"Updated population of Berlin: {berlin.population}")
print(f"Landmarks in Berlin: {berlin.landmarks}")

# Remove a city from Germany
germany.remove_city(frankfurt)

# Show the updated country details in the menu
menu.show_country(germany)
menu.show_country(france)
menu.show_country(italy)

