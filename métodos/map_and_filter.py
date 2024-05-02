def sum_2(n):
    return n + 2


def bigger_than_10(n):
    return n > 10


# Map - applies the function specified for each element from the iterable provided and returns the results.
print(list(map(sum_2, [0, 1, 2, 3])))

# Filter - applies the function specified for each element from the iterable and returns only the True results.
print(list(filter(bigger_than_10, [8, 9, 11, 12])))
