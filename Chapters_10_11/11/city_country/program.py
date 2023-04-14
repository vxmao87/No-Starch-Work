# 11-1, 11-2
from city_functions import get_formatted_city_country

print("Enter 'q' at any time to quit.")
while True:

  city = input("\nPlease give me the name of a city: ")
  if city == 'q':
    break

  country = input("\nGive me the name of a country: ")
  if country == 'q':
    break

  formatted_city_country = get_formatted_city_country(city, country)
  print(f"\nOur neatly formatted text: {formatted_city_country}")
