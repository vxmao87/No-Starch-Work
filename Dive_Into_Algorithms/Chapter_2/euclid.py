def gcd(x, y):
    larger = max(x, y)
    smaller = min(x, y)

    remainder = larger % smaller

    if remainder == 0:
        return smaller
    else:
        return gcd(smaller, remainder)


def main():
    print(gcd(105, 33))


main()

"""
Notes:
The implementation of Euclid's algorithm uses recursion. The algorithm finds the greatest
common divisor between two given numbers as follows:

Divide the larger number (a) by the smaller number (b), then take the answer (q1) and remainder
(c) and rearrange as follows:

a = q1 * b + c

You will then divide b by c and get a new quotient and remainder which you will then set up 
exactly as above.

This process repeats until you get a remainder that is zero.

The last nonzero remainder you got will be the greatest common divisor between the two numbers.
"""
