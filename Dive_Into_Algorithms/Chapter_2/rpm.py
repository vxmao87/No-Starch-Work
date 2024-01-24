import math
import pandas as pd


def rpm(n1, n2):
    """
    Perform Russian peasant multiplication by doing the following given n1 and n2:

    Halve n1 repeatedly while dropping the remainder until you reach 1.
    Double n2 the same number of times as there are numbers in the halving list,
    Remove all pairs such that the halving number is even.
    Add all the remaining values in the doubling column together to get your answer.
    """
    halving = [n1]
    while min(halving) > 1:
        halving.append(math.floor(min(halving) / 2))

    doubling = [n2]
    while len(doubling) < len(halving):
        doubling.append(max(doubling) * 2)

    half_double = pd.DataFrame(zip(halving, doubling))
    half_double = half_double.loc[half_double[0] % 2 == 1, :]
    answer = sum(half_double.loc[:, 1])
    return answer


def main():
    print(rpm(89, 18))


main()

# Notes:
# It is actually better for n1 to be smaller and n2 to be bigger to perform this algorithm in fewer
# steps. At the same time, using this method can help you find the binary values of such regular
# numbers.
