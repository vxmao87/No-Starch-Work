import random

# 8-15, 8-16, 8-17
def print_all_numbers(num):
    """
    Prints all numbers from 1 to the specified parameter.
    """
    for i in range(1, num):
        print(i)

def send_number_list(times):
    """
    Returns a randomly generated number list.
    """
    new_list = []
    for _ in range(times):
        new_list.append(random.randint(1, 20))
    return new_list