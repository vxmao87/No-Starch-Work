# 8-1
def display_message():
    print("Remember to call your functions or this won't show up!")

# 8-2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

# 8-3, 8-4
def make_shirt(size="L", text="I love Python"):
    print(f"Shirt size: {size}")
    print(f"Text: {text}")

# 8-5
def describe_city(city, country="the United States"):
    print(f"{city.title()} is in {country.title()}.")

# 8-6
def city_country(city, country):
    return f"{city.title()}, {country.title()}"

# 8-7
def make_album(artist, album_title, num_tracks=None):
    if num_tracks:
        return {
            "name": artist,
            "album": album_title,
            "num_tracks": num_tracks
        }
    else:
        return {
          "name": artist,
          "album": album_title
        }
    
# 8-8
def get_formatted_album_name(artist, album):
    return f"{artist} - {album}"

# 8-9, 8-10, 8-11
def show_message(message):
    print(message)

# 8-10, 8-11
def send_messages(message_list, sent_messages):
    while message_list:
        sent_message = message_list.pop()
        show_message(sent_message)
        sent_messages.append(sent_message)

# 8-12
def make_sandwich(*toppings):
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# 8-13
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

# 8-14
def make_car(brand, model, **car_info):
    car_info["brand"] = brand
    car_info["model"] = model
    return car_info

# 8-15, 8-16, 8-17
# This should normally be at the beginning of this whole file.
# import random_module
# from random_module import print_all_numbers
# from random_module import send_number_list as send_list
# import random_module as rm
# from random_module import *

display_message()
favorite_book("Becoming by Michelle Obama")
make_shirt("M", "Happy Friday!")
make_shirt(text="Calculus beast", size="L")
make_shirt()
make_shirt(size="M")
make_shirt(size="S", text="I love Java and JavaScript")
describe_city("Seattle")
describe_city("San FRancisco")
describe_city("Beijing", country="China")
print(city_country("Shanghai", "China"))
print(make_album("Beyonce", "Dangerously in Love"))
print(make_album("Rihanna", "Talk That Talk", num_tracks=15))
print(make_album("Alicia Keys", "As I Am"))
print(make_album("Macy Gray", "Sellout"))

typed_messages = [
    "Let's hang out!",
    "Wyd",
    "Ttyl, good night!"
]
sent_messages = []
send_messages(typed_messages[:], sent_messages)
print(typed_messages)
print(sent_messages)

make_sandwich("beef")
make_sandwich("lettuce", "bacon", "tomatoes")
make_sandwich("chicken patty", "mayo", "secret sauce", "lettuce")

user_profile = build_profile(
    "Vinh",
    "Mao",
    location="Seattle",
    favorite_game="Groove Coaster",
    favorite_place="Gas Works Park")
print(user_profile)

car_profile = make_car(
    "Toyota",
    "Camry",
    color="silver",
    year=2015,
    tow_package=True
)
print(car_profile)

# # For 8-8
# while True:
#     print("\nEnter an artist's name: ")
#     print("(enter 'q' at any time to quit) ")

#     artist = input("Artist name: ")
#     if artist == 'q':
#         break
    
#     album_name = input("Album name: ")
#     if album_name == 'q':
#         break
    
#     print(get_formatted_album_name(artist, album_name))
    

