# 4-1
favorite_pizzas = ["pepperoni", "Hawaiian", "meat lover's"]
for pizza in favorite_pizzas:
	print(f"I love {pizza} pizza!")

print("I love pizza too much!")
print("I need it veery day")
print("Let's go to Domino's, Pizza Hut and Papa John's!")

# 4-2
some_animals = ["tiger", "bear", "wolf"]
for animal in some_animals:
	print(f"A {animal} is dangerous.")

print("These animals would not make great pets!")

# 4-3
for i in range(1, 21):
	print(i)

# 4-4
large_numbers = list(range(1, 1_000_001))
# for large_number in large_numbers:
#   print(large_number)

# 4-5
print(min(large_numbers))
print(max(large_numbers))
print(sum(large_numbers))

# 4-6
for j in range(1, 21, 2):
	print(j)

# 4-7
three_multiples = [num for num in range(3, 31) if num % 3 == 0]
print(three_multiples)

# 4-8, 4-9
cube_multiples = [num**3 for num in range(1, 11)]
for cube_multiple in cube_multiples:
	print(cube_multiple)

# 4-10
first_three_multiples = three_multiples[:3]
middle_three_multiples = three_multiples[4:7]
last_three_multiples = three_multiples[-3:]
print("The first three multiples of 3 are:")
print(first_three_multiples)
print("\nThe middle three multiples of 3 are:")
print(middle_three_multiples)
print("\nFinally, the last three multiples of 3 are:")
print(last_three_multiples)

# 4-11
friends_pizzas = favorite_pizzas[:]
favorite_pizzas.append("brioche")
friends_pizzas.append("BBQ")
print("\nMy favorite pizzas are:")
print(favorite_pizzas)
print("\nMy friend's favorite pizzas are:")
print(friends_pizzas)

# 4-12
my_foods = ["pizza", "falafel", "carrot cake"]
friends_foods = my_foods[:]

for food in my_foods:
	print(food)

for food in friends_foods:
	print(food)

# 4-13
buffet_foods = ("banh xeo", "banh mi", "bun bo hue", "bun rieu", "che 3 mau")
print(buffet_foods)
# # Can't modify tuple: confirmed
# buffet_foods[2] = "goi cuon"
buffet_foods = ("banh xeo", "com tam suon bo", "bun bo hue", "bun rieu", "bun cha Hanoi")
for viet_food in buffet_foods:
	print(viet_food)

# 5-1, 5-2
code = "Python"
another_code = "TypeScript"
yet_another_code = "python"
large_integer = 256
car_model = "KoenigSeGG"
small_integer = 8
current_integer_1 = 3
current_integer_2 = 128
current_integer_3 = 256
puzzle_games = ["Sudoku", "Kakuro", "Jumble"]
print("Is code == Python? I think True")
print(code == "Python")
print("\nIs code == Ruby? I think False")
print(code == "Ruby")
print("\n")
print(code == another_code)
print(code == yet_another_code)
print(code.lower() == yet_another_code)
print(current_integer_1 < small_integer and current_integer_1 < large_integer)
print(current_integer_2 <= small_integer or current_integer_2 > large_integer)
print(current_integer_3 >= small_integer and current_integer_3 >= large_integer)
print("Kakuro" in puzzle_games)
print("Chess" in puzzle_games)

# 5-3
alien_color_1 = "green"
if alien_color_1 == "green":
	print("You earned 5 points!")

if alien_color_1 == "red":
	print("You earned 10 points!")
elif alien_color_1 == "blue":
	print("You earned 20 points!")

# 5-4
alien_color_2 = "yellow"
if alien_color_2 != "yellow":
	print("You earned 7 points!")
else:
	print("You earned -1 points!")

if alien_color_2 == "yellow":
	print("You earned -23 points!")
else:
	print("You lost 2 * 50 points!")

# 5-5
alien_color_3 = "red"

if alien_color_3 == "red":
	points_1 = 15
elif alien_color_3 != "green":
	points_1 = 5
else:
	points_1 = 10

if alien_color_3 == "yellow":
	points_2 = 10
elif alien_color_3 != "green":
	points_2 = 15
else:
	points_2 = 5

if alien_color_3 == "green":
	points_3 = 5
elif alien_color_3 == "yellow":
	points_3 = 10
else:
	points_3 = 15

print(f"You earned {points_1} points in Game 1!")
print(f"You earned {points_2} points in Game 2!")
print(f"You earned {points_3} points in Game 3!")

# 5-6
your_age = 30

if your_age > 0:
	if your_age < 2:
		life_stage = "baby"
	elif your_age >= 2 and your_age < 4:
		life_stage = "toddler"
	elif your_age >= 4 and your_age < 13:
		life_stage = "kid"
	elif your_age >= 13 and your_age < 20:
		life_stage = "teenager"
	elif your_age >= 20 and your_age < 65:
		life_stage = "adult"
	elif your_age >= 65:
		life_stage = "elder"
	print(f"You are a(n) {life_stage}!")
else:
	print("Code does not work.")

# 5-7
favorite_fruits = ["apples", "bananas", "oranges", "grapes", "strawberries"]
if "apples" in favorite_fruits:
	print("Wow, you really love apples!")

if "bananas" in favorite_fruits:
	print("Wow, you really love bananas!")

if "oranges" in favorite_fruits:
	print("Wow, you really love oranges!")

if "grapes" in favorite_fruits:
	print("Wow, you really love grapes!")

if "strawberries" in favorite_fruits:
	print("Wow, you really love strawberries!")

# 5-8, 5-9
current_username_list = ["spongeisbob", "admin", "sashafierce", "Fastfurious", "aslmaster"]
# del current_username_list[0]
# del current_username_list[0]
# del current_username_list[0]
# del current_username_list[0]
# del current_username_list[0]
if current_username_list:
	for username in current_username_list:
		if username == "admin":
			print("Welcome admin, would you like to see s status report?")
		else:
			print(f"Hello {username}, welcome back!")
else:
	print("We need more users!")

# 5-10
new_username_list = ["strbcks", "extraordin", "optimismBrew", "fastfurious", "ASLmaster"]
current_username_copy = [name.lower() for name in current_username_list]

for new_user in new_username_list:
	if new_user.lower() in current_username_copy:
		print("Sorry, this username is unavailable!")
	else:
		print("Username is available!")

# 5-11
integers = list(range(1, 10))
for num in integers:
	if num == 1:
		print(f"{num}st")
	elif num == 2:
		print(f"{num}nd")
	elif num == 3:
		print(f"{num}rd")
	else:
		print(f"{num}th")

"""
5-12 involves styling our conditionals correctly, which are only to make sure
there are spaces between the conditionals we write.

5-13 requires no code.
"""