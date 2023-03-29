# Chapter 1
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