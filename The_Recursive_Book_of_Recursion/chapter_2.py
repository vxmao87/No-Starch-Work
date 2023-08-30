# 1
def sum_series(n):
    result = 0
    for i in range(1, n + 1):
        result = result + i
    return result


# 2
def sum_series_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_series_recursive(n - 1)


# 3  
def sum_powers_of_2(n):
    result = 0
    for i in range(1, n + 1):
        result += 2 ** i
    return result


# 4
def sum_powers_of_2_recursive(n):
    if n == 1:
        return 2
    else:
        return (2 ** n) + sum_powers_of_2_recursive(n - 1)


print(sum_series(2))
print(sum_series_recursive(2))
print(sum_powers_of_2(5))
print(sum_powers_of_2_recursive(5))
