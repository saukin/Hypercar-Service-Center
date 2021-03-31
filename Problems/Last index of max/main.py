def last_indexof_max(numbers):
    index = -1
    for i in range(0, len(numbers)):
        if numbers[i] >= numbers[index]:
            index = i

    return index
