import unittest
import city_functions
# 11-1. City, Country: Write a function that accepts two parameters: a city name
# and a country name. The function should return a single string of the form
# City, Country , such as Santiago, Chile . Store the function in a module called
# city_functions.py.
# Create a file called test_cities.py that tests the function you just wrote
# (remember that you need to import unittest and the function you want to test).
# Write a method called test_city_country() to verify that calling your function
# with values such as 'santiago' and 'chile' results in the correct string. Run
# test_cities.py, and make sure test_city_country() passes.
class testCities (unittest.TestCase):

    def test_city_country_columbus(self):
        city = "columbus"
        country = "united states"
        result = "Columbus, United States"
        self.assertEqual(city_functions.city_country(city,country), result)

    def test_city_country_santiago(self):
        city = "santiago"
        country = "chile"
        result = "Santiago, Chile - population 500000"
        self.assertEqual(city_functions.city_country(city,country, 500000), result)

    if __name__ == '__main__':
        unittest.main()
