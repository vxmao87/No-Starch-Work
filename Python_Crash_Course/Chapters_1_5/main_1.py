# Chapter 1
import random


print("Hello Python world!")

# Chapter 2
message = "Hello to this world!"
print(message)
message = "Hello to this big world!"
print(message)

# 2-1, 2-2
name = "kevin zhu"
print(name.title())
print(name.upper())
print(name.lower())

# 2-3
friend_name = "Alan Chan"
print(f"Hey {friend_name}, how's it going?")

# 2-4
base_name = "freddy rogers"
print(base_name.title())
print(base_name.upper())
print(base_name.lower())

# 2-5, 2-6
famous_person = "Beyonce"
message = "Power is not given to you. You have to take it."
print(f'{famous_person} once said, "{message}"')

# 2-7
person = "  Sabrina\n\tGreen   "
print(person.rstrip())
print(person.lstrip())
print(person.strip())

# 2-8
no_starch_url = "https://nostarch.com"
print(no_starch_url.removeprefix("https://"))

# Removes the suffix of the given string
file_url = "python_notes.txt"
print(file_url.removesuffix(".txt"))

# 2-9 
print(5 + 3)
print(10 - 2)
print(2 * 4)
print(16 / 2)

# 2-10
favorite_number = 256
print(f"My favorite number is {favorite_number}!")

# 2-11 is adding comments as above.

# 2-12
"""
The following output occurs after running 'import this' in the Terminal:

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# 3-1
friend_names = ["Kevin", "Jacky", "Andrew", "Perry"]
print(friend_names[0])
print(friend_names[1])
print(friend_names[2])
print(friend_names[3])

# 3-2
print(f"Hey, {friend_names[0]}, nice weather we got?")
print(f"Hey, {friend_names[1]}, nice weather we got?")
print(f"Hey, {friend_names[2]}, nice weather we got?")
print(f"Hey, {friend_names[3]}, nice weather we got?")

# 3-3
vehicles = ["motorcycle", "car", "bus", "bike"]
car_brands = ["Honda", "Toyota", "Audi", "BMW", "Ferrari"]
rand_vehicle = random.randint(0, 3)
rand_brand = random.randint(0, 4)
print(f"I'd like to own a(n) {car_brands[rand_brand]} {vehicles[rand_vehicle]} someday!")

# 3-4
famous_people = ["Beyonce", "RM", "Keanu Reeves"]
print(f"Hey {famous_people[0]}, let's have dinner!")
print(f"Hey {famous_people[1]}, let's have dinner!")
print(f"Hey {famous_people[2]}, let's have dinner!")

# 3-5
print(f"Oh no, {famous_people.pop(1)} isn't able to make it!")
famous_people.insert(1, "Michelle Yeoh")
print(f"But {famous_people[1]} can join instead!")
print(f"Okay {famous_people[0]}, let's have dinner!")
print(f"Okay {famous_people[1]}, let's have dinner!")
print(f"Okay {famous_people[2]}, let's have dinner!")

# 3-6
print("Wait there's a bigger table now!")
famous_people.insert(0, "Alicia Keys")
famous_people.insert(2, "Dan Levy")
famous_people.append("Rihanna")
for person in famous_people:
  print(f"All right {person}, let's finally have dinner!")

# 3-9
print(len(famous_people))

# 3-7
print("Sorry everyone, only two people can be at my dinner table now!")
while len(famous_people) > 2:
  print(f"Sorry {famous_people.pop()}, I won't be able to invite you! Next time?")

for person in famous_people:
  print(f"Hey {person} you're still invited to my dinner table!")

del famous_people[0]
del famous_people[0]
print(famous_people)

# 3-8
places_to_visit = ["Japan", "new York", "Chicago", "Hong Kong", "London"]
print(places_to_visit)
print(sorted(places_to_visit))
print(sorted(places_to_visit, reverse=True))
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.sort()
print(places_to_visit)
places_to_visit.sort(reverse=True)
print(places_to_visit)

# 3-10
rhythm_games = ["Groove Coaster", "Arcaea", "WACCA", "CHUNITHM", "DanceRush", "Sound Voltex"]
print(rhythm_games)
rhythm_games[2] = "Chrono Circle"
print(rhythm_games)
rhythm_games.append("WACCA")
print(rhythm_games)
rhythm_games.insert(3, "DDR")
print(rhythm_games)
popped_game = rhythm_games.pop()
print(popped_game)
print(rhythm_games)
del rhythm_games[2]
print(rhythm_games)
last_game = rhythm_games.pop(-1)
print(last_game)
print(rhythm_games)
rhythm_games.remove("CHUNITHM")
print(rhythm_games)
print(sorted(rhythm_games))
print(sorted(rhythm_games, reverse=True))
rhythm_games.reverse()
print(rhythm_games)
rhythm_games.reverse()
print(rhythm_games)
rhythm_games.sort(reverse=True)
print(rhythm_games)
rhythm_games.sort()
print(rhythm_games)

# 3-11
print(famous_people)
# # This will print an error because the list is empty.
# print(famous_people[0])
