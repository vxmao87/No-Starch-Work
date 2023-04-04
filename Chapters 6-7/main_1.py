# 6-1
friend_info_1 = {
    "first_name": "Jacky",
    "last_name": "Cheung",
    "age": 29,
    "city": "Seattle",
}
print(friend_info_1["first_name"])
print(friend_info_1["last_name"])
print(friend_info_1["age"])
print(friend_info_1["city"])

# 6-2
favorite_numbers = {
    "Andy": 7,
    "Jason": 9,
    "Perry": 8,
    "Aaron": 13,
    "Robbie": 3,
}
print(f"Andy's favorite number is {favorite_numbers['Andy']}.")
print(f"Jason's favorite number is {favorite_numbers['Jason']}.")
print(f"Perry's favorite number is {favorite_numbers['Perry']}.")
print(f"Aaron's favorite number is {favorite_numbers['Aaron']}.")
print(f"Robbie's favorite number is {favorite_numbers['Robbie']}.")

# 6-3
python_commands = {}
python_commands["if/else"] = "for conditionals"
python_commands["while"] = "loop that runs until a condition is met"
python_commands["del"] = "used to delete key/value pairs, list values, etc."
# print(f"if/else:\n\t{python_commands['if/else']}")
# print(f"while:\n\t{python_commands['while']}")
# print(f"del:\n\t{python_commands['del']}")

# 6-4
for command, definition in python_commands.items():
  print(f"{command}:\n\t{definition}")

# 6-5
major_rivers = {
  "Yellow": "China",
  "Nile": "Egypt",
  "Thames": "United Kingdom"
}
for river, country in major_rivers.items():
  print(f"The {river} River runs through {country}.")

for river in major_rivers.keys():
  print(river)

for country in set(major_rivers.values()):
  print(country)

# 6-6
list_of_friends = ["Robbie", "Jackson", "George", "Andy", "Perry"]
for name in list_of_friends:
  if name not in favorite_numbers.keys():
    print(f"{name}, please take our favorite numbers poll!")
  else:
    print(f"Hey {name}, you said your favorite number is {favorite_numbers[name]}, right?")

# 6-7
friend_info_2 = {
    "first_name": "Kevin",
    "last_name": "Lu",
    "age": 27,
    "city": "Bellevue",
}
friend_info_3 = {
    "first_name": "Alex",
    "last_name": "Gan",
    "age": 26,
    "city": "Tukwila",
}

my_friends = [friend_info_1, friend_info_2, friend_info_3]
for friend in my_friends:
  first_name = friend["first_name"]
  last_name = friend["last_name"]
  age = friend["age"]
  city = friend["city"]
  print(f"This is my friend {first_name} {last_name}! He's {age} years old "
        f"and lives in {city}!")
  
# 6-8
pets_list = [
  {
    "pet": "gecko",
    "owner_name": "Sarah"
  },
  {
    "pet": "hamster",
    "owner_name": "Esther"
  },
  {
    "pet": "corgi",
    "owner_name": "Amy"
  }
]

for pet in pets_list:
  owner_name = pet["owner_name"]
  pet_type = pet["pet"]
  print(f"{owner_name} owns a pet {pet_type}!")

# 6-9
favorite_places = [
  {
    "name": "Rayna",
    "places": ["Barcelona", "Tokyo", "Chengdu"]
  },
  {
    "name": "Beth",
    "places": ["Lima", "Bangkok", "Taipei"]
  },
  {
    "name": "Paula",
    "places": ["Hong Kong", "London", "Paris"]
  }
]
for person in favorite_places:
  print(f"\n{person['name']}'s favorite places are:")
  for place in person["places"]:
    print(f"\t{place.title()}")

# 6-10
favorite_numbers["Andy"] = [7, 8, 9, 10]
favorite_numbers["Jason"] = [33]
favorite_numbers["Perry"] = [7]
favorite_numbers["Aaron"] = [13, 14]
favorite_numbers["Robbie"] = [2, 5]

for name, nums in favorite_numbers.items():
  if len(nums) > 1:
    print(f"{name}'s favorite numbers are:")
    for num in nums:
      print(f"\t{num}")
  else:
    print(f"{name}'s favorite number is {nums[0]}")

# 6-11 (facts below are inaccurate)
best_cities = {
  "Hong Kong": {
    "country": "China",
    "population": 2_500_000,
    "fact": "Hong Kong means 'fragrant harbor' in Chinese."
  },
  "Tokyo": {
    "country": "Japan",
    "population": 37_000_000,
    "fact": "Tokyo has a robot hotel!"
  },
  "Sydney": {
    "country": "Australia",
    "population": 950_000,
    "fact": "Sydney has one of the longest steel bridges in the world."
  },
  "London": {
    "country": "United Kingdom",
    "population": 8_500_000,
    "fact": "About 6.5 million people take the bus in London every day!"
  },
  "Chicago": {
    "country": "United States",
    "population": 1_250_000,
    "fact": "House music was first produced in Chicago."
  },
}

for city, city_info in best_cities.items():
  country = city_info["country"]
  population = city_info["population"]
  fact = city_info["fact"]
  print(f"\nCity: {city}")
  print(f"\tLocated in: {country}")
  print(f"\tPopulation (very, very inaccurate): {population}")
  print(f"Fact: {fact}")

# 6-12

# # 7-1
# car_message = input("What kind of rental car would you like? ")
# print(f"Let me see if I can find you a(n) {car_message}...")

# # 7-2
# num_of_people = int(input("How many people are in your table? "))
# if num_of_people > 8:
#   print("You'll need to wait for a table. Wait time is about 5 hours.")
# else:
#   print("Yes we have a table ready for you!")

# # 7-3
# num_for_10 = int(input("Please give me a number: "))
# if num_for_10 % 10 == 0:
#   print("This number is divisible by 10!")
# else:
#   print("This number is NOT divisible by 10.")

# # 7-4
# prompt = "\nGive me a pizza topping to add:"
# prompt += "\nEnter 'quit' to exit this program. "
# message = ""
# while message != "quit":
#   message = input(prompt)

#   if message != "quit":
#     print(f"Let me add some {message} for you!")

# # 7-5
# prompt = "How old are you? "
# age_input = int(input(prompt))
# if age_input > 0:
#   if age_input < 3:
#     print("Your ticket is free!")
#   elif age_input >= 3 and age_input <= 12:
#     print("Your ticket is $10.")
#   elif age_input > 12:
#     print("Your ticket is $15.")
# else:
#   print("You have just typed an invalid number.")

# 7-6
# prompt = "How old are you? "
# active = True
# while active:
#   age_input = int(input(prompt))
#   if age_input > 0:
#     if age_input < 3:
#       print("Your ticket is free!")
#     elif age_input >= 3 and age_input <= 12:
#       print("Your ticket is $10.")
#     elif age_input > 12:
#       print("Your ticket is $15.")
#   else:
#     active = False

# prompt = "How old are you? "
# active = True
# tries = 0
# while active:
#   tries += 1
#   if tries > 3:
#     active = False
#   age_input = int(input(prompt))
#   if age_input > 0:
#     if age_input < 3:
#       print("Your ticket is free!")
#     elif age_input >= 3 and age_input <= 12:
#       print("Your ticket is $10.")
#     elif age_input > 12 and age_input <= 125:
#       print("Your ticket is $15.")
#     else:
#       break
#   else:
#     print("Please try another number!")
#     continue

#   print("Another successful try!")

# # 7-7
# while 5 == 1:
#   print("Let's do this!")

# 7-8
sandwich_orders = ["BLT", "avocado toast", "Nashville sandwich"]
finished_sandwiches = []

while sandwich_orders:
  current_sandwich = sandwich_orders.pop()
  print(f"I'm making your {current_sandwich} now!")
  finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made: ")
for sandwich in finished_sandwiches:
  print(sandwich)

# 7-9
sandwich_orders = ["pastrami", "BLT", "pastrami", "avocado toast", "Nashville sandwich", "pastrami"]
print(sandwich_orders)
while "pastrami" in sandwich_orders:
  sandwich_orders.remove("pastrami")
print(sandwich_orders)

# 7-10
responses = {}
polling_active = True

while polling_active:
  name = input("What is your name? ")
  response = input("Where would you like to go on a dream vacation? ")

  responses[name] = response

  repeat = input("Would you like to let another person respond? (yes/no) ")
  if repeat.lower() == "no":
    polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
  print(f"{name} would like to go {response} for their dream vacation!")