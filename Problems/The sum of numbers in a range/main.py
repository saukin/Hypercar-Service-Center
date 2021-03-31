def range_sum(numbers, start, end):
    _sum = 0
    for i in numbers:
        if start <= i <= end:
            _sum += i
    return _sum


input_numbers = [int(x) for x in input().split(" ")]
a, b = [int(x) for x in input().split(" ")]
print(range_sum(input_numbers, a, b))
