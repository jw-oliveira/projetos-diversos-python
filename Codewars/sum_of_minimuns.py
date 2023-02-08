def sum_of_minimums(numbers):
    sum = 0
    for list in numbers: sum += min(list)

    return sum