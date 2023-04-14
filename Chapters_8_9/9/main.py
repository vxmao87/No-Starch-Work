from restaurant import Restaurant, IceCreamStand
from user import User
from car import ElectricCar
from admin import Admin
from die import Die
from random import randint

# 9-2
rest_1 = Restaurant("The Dolar Shop", "Chinese")
rest_2 = Restaurant("Momiji", "Japanese")
rest_3 = Restaurant("The Alley", "Korean")
rest_1.describe_restaurant()
rest_2.describe_restaurant()
rest_3.describe_restaurant()

# 9-3
user_1 = User("Alex", "Tam", 29, "atam88")
user_2 = User("Lynna", "Nguyen", 26, "lnguyen")
user_3 = User("Harris", "Cheung", 30, "harrisc345")
user_1.describe_user()
user_2.describe_user()
user_3.describe_user()

# 9-4
print(f"{rest_1.restaurant_name} has served {rest_1.number_served} people.")
rest_1.number_served = 10
print(f"Now {rest_1.restaurant_name} has served {rest_1.number_served} people.")
rest_1.set_number_served(15)
print(f"Actually, {rest_1.restaurant_name} has served {rest_1.number_served} people. Whoops!")
rest_1.increment_number_served(85)
print(f"After a day, {rest_1.restaurant_name} has served {rest_1.number_served} people.")

# 9-5
print(f"{user_1.username} has been logged into {user_1.login_attempts} times.")
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"{user_1.username} has been logged into {user_1.login_attempts} times.")
user_1.reset_login_attempts()
print(f"{user_1.username} has been logged into {user_1.login_attempts} times.")

# 9-6
ice_cream_stand = IceCreamStand("Molly Moon's", "American")
ice_cream_stand.display_flavors()

# 9-7, 9-8
admin_1 = Admin("Chris", "Chang", 29, "chrischang159")
admin_1.privileges.show_privileges()

# 9-9
electric_car = ElectricCar("Nissan", "Leaf", 2024)
electric_car.get_range()
electric_car.battery.upgrade_battery()
electric_car.get_range()

# 9-13
dice_6 = Die()
dice_10 = Die(10)
dice_20 = Die(20)

for _ in range(10):
    dice_6.roll_dice()
    dice_10.roll_dice()
    dice_20.roll_dice()

# 9-14, 9-15
lottery_set = ["E", "A", "5", "1", "D", "4", "B", "2", "3", "C"]
lottery_copy = lottery_set[:]
lottery_goal = []

for _ in range(4):
    lottery_index = randint(0, len(lottery_copy) - 1)
    lottery_draw = lottery_copy.pop(lottery_index)
    lottery_goal.append(lottery_draw)

print(lottery_goal)

draws = 0

active = True
while active:
    draws += 1
    lottery_copy_2 = lottery_set[:]
    lottery_obtain = []

    for _ in range(4):
      lottery_index_2 = randint(0, len(lottery_copy_2) - 1)
      lottery_draw_2 = lottery_copy_2.pop(lottery_index_2)
      lottery_obtain.append(lottery_draw_2)

    correct = 0
    for char in lottery_obtain:
        if char not in lottery_goal:
            continue
        else:
            correct += 1

    if correct == 4:
        active = False

print(draws)

