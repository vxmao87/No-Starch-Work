# 11-1, 11-2
def get_formatted_city_country(city, country, population=""):
  """
  Prints the city and country (and population) in a neat format.
  """
  if population:
    return f"{city}, {country} - Population {population}".title()
  else:
    return f"{city}, {country}".title()
    
