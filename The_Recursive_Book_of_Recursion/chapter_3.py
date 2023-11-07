import sys

# 1
def concat(words):
    if len(words) == 0:
        return ''
    else:
        head = words[0]
        tail = words[1:]
        return head + concat(tail)


print(concat(['Hello', 'World']))
print(concat(['Randy', 'Is', 'A', 'Stooge']))


# 2
def product(numbers):
    if len(numbers) == 0:
        return 1
    elif len(numbers) == 1:
        return numbers[0]
    else:
        head = numbers[0]
        tail = numbers[1:]
        return head * product(tail)
    

# 3
def flood_fill(image, x, y, newChar, oldChar=None):
    if oldChar == None:
        oldChar = image[y][x]
    if oldChar == newChar or image[y][x] != oldChar:
        return
    
    image[y][x] = newChar

    print_image(image)

    if y + 1 < HEIGHT and image[y + 1][x] == oldChar:
        flood_fill(image, x, y + 1, newChar, oldChar)
    if y - 1 >= 0 and image[y - 1][x] == oldChar:
        flood_fill(image, x, y - 1, newChar, oldChar)
    if x + 1 < WIDTH and image[y][x + 1] == oldChar:
        flood_fill(image, x + 1, y, newChar, oldChar)
    if x - 1 >= 0 and image[y][x - 1] == oldChar:
        flood_fill(image, x - 1, y, newChar, oldChar)
    return

def print_image(image):
    with open('The_Recursive_Book_of_Recursion/assets/3_3.txt', 'a+') as file:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                file.write(image[y][x])
            file.write('\n')
        file.write('\n')

def count_rooms(image):
    count = 0
    for y, i in enumerate(image):
        for x, j in enumerate(i):
            if j == '.':
                count += 1
                flood_fill(image, x, y, 'o', oldChar=None)
    return count
    

print(product([2, 4, 5]))
print(product([8, 16, 24, 32, 40]))

im = [list('...##########....................................'),
      list('...#........#....####..................##########'),
      list('...#........#....#..#...############...#........#'),
      list('...##########....#..#...#..........#...##.......#'),
      list('.......#....#....####...#..........#....##......#'),
      list('.......#....#....#......############.....##.....#'),
      list('.......######....#........................##....#'),
      list('.................####........####..........######')] 

HEIGHT = len(im)
WIDTH = len(im[0])

print(f'There are {count_rooms(im)} rooms in the given image.')
