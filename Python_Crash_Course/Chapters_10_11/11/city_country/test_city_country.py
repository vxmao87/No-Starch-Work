from city_functions import get_formatted_city_country

# 11-1
def test_city_country():
  formatted_city_country = get_formatted_city_country("shanghai", "china")
  assert formatted_city_country == "Shanghai, China"

# 11-2
def test_city_country_population():
  formatted_city_country_pop = get_formatted_city_country("shanghai", "china", "50,000,000")
  assert formatted_city_country_pop == "Shanghai, China - Population 50,000,000"