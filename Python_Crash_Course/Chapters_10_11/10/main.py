from pathlib import Path
import json

# 10-1
learning_python_path = Path('Chapters 10-11/10/learning_python.txt')
learning_python_contents = learning_python_path.read_text()

print(learning_python_contents)

# learning_python_lines = learning_python_contents.splitlines()
# for learning_python_line in learning_python_lines:
#     print(learning_python_line)

#     # 10-2
#     new_learning_line = learning_python_line.replace("Python", "JavaScript")
#     print(new_learning_line)

# 10-3
for learning_python_line in learning_python_contents.splitlines():
	print(learning_python_line)

    # 10-2
	new_learning_line = learning_python_line.replace("Python", "JavaScript")
	print(new_learning_line)

# 10-4, 10-5
active = True
guests_string = ""

while True:
    print("Give me a guest name!")
    guest_name = input("(Enter 'q' to quit): ")

    if guest_name == 'q':
        break
    else:
        guests_string += f"\n{guest_name}"


guest_path = Path('Chapters 10-11/10/guest_list.txt')
guest_path.write_text(guests_string.lstrip())

# 10-6, 10-7
def add_numbers(num_1, num_2):
	"""
  Adds the two user-inputted values if they are numbers.
  """
	try:
		sum_nums = int(num_1) + int(num_2)
	except ValueError:
		print("One of these values is NOT a number!")
	else:
		print(sum_nums)

active_2 = True
while active_2:
    num_1 = input("Give me a number: ")
    if num_1 == 'q':
        break

    num_2 = input("Give me another number: ")
    if num_2 == 'q':
        break

    add_numbers(num_1, num_2)
      
# 10-8
pet_filenames = ["Chapters 10-11/10/cats.txt", "Chapters 10-11/10/dogs.txt"]
for pet_file in pet_filenames:
	try:
		pet_path = Path(pet_file)
		pet_contents = pet_path.read_text()
	except FileNotFoundError:
		# 10-9
		pass
	else:
		for pet_line in pet_contents.splitlines():
			print(pet_line)

# 10-10
def count_words(book_contents, word):
	"""
  Counts the number of times the given word is in the file.
  """
	total_count = 0
	for book_line in book_contents.splitlines():
		total_count += book_line.lower().count(word)

	return total_count

books_list = [
	"Chapters 10-11/10/egyptian_oasis.txt",
	"Chapters 10-11/10/to_let.txt",
	"Chapters 10-11/10/angels_brother.txt",
	"Chapters 10-11/10/tumbling_river_range.txt"
]
for book in books_list:
	try:
		book_path = Path(book)
		book_contents = book_path.read_text()
	except FileNotFoundError:
		print("Sorry, this file does not exist!")
	else:
		print(count_words(book_contents, "there"))

# 10-11, 10-12
def get_favorite_number(path):
	"""
  Grabs the person's favorite number if it exists.
  """
	if path.exists():
		contents = path.read_text()
		favorite_number = json.loads(contents)
		return favorite_number
	else:
		return None
	
def get_new_fav_number(path):
	"""
  Creates a new favorite number for a new user.
  """
	favorite_number = input("Give me your favorite number: ")
	contents = json.dumps(favorite_number)
	path.write_text(contents)
	return favorite_number

def display_fav_number():
	"""
  Displays the current person's favorite number, or assigns one to them.
  """
	favorite_number_path = Path("Chapters 10-11/10/favorite_numbers.json")
	favorite_number = get_favorite_number(favorite_number_path)
	if favorite_number:
		print(f"I know your favorite number! It's {favorite_number}.")
	else:
		favorite_number = get_new_fav_number(favorite_number_path)
		print(f"I'll remember {favorite_number} as your favorite number!")

display_fav_number()

# 10-13, 10-14
def get_stored_info(user_path):
  """
  Obtains any stored user information.
  """
  if user_path.exists():
    user_contents = user_path.read_text()
    info = json.loads(user_contents)
    return info
  else:
    return None

def obtain_info(user_path):
	"""
  Asks for new info and inputs them into a JSON.
  """
	username = input("What is your name? ")
	favorite_city = input("What's one of your favorite cities? ")
	pet_peeve = input("What's one of your pet peeves? ")
	info = {
		"username": username,
		"favorite_city": favorite_city,
		"pet_peeve": pet_peeve
  }
	contents = json.dumps(info)
	user_path.write_text(contents)
	return info

def get_new_info(user_path):
  """
  Grabs new info from the user and prints them out.
  """
  info = obtain_info(user_path)
  print(f"We'll remember you when you come back, {info['username']}!")
  print(f"You said your favorite city is {info['favorite_city']}!")
  print(f"And your pet peeve is: {info['pet_peeve']}")

def greet_user():
  """
  Greets the user by checking if there is info inside the JSON file, or 
  creating new info by asking the user for some input.
  """
  path = Path('Chapters 10-11/10/user_info.json')
  info = get_stored_info(path)
  if info:
    correct_user = input(f"Is {info['username']} the correct user? Type 'y'/'n': ")
    if correct_user.lower() == "y":
      print(f"Welcome back, {info['username']}!")
      print(f"Your favorite city is {info['favorite_city']}.")
      print(f"Your pet peeve: {info['pet_peeve']}")
    else:
      get_new_info(path)
  else:
    get_new_info(path)
		
greet_user()