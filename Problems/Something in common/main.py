def calculate_linear(k, b, x):
    y = k * x + b
    return y


def calculate_quadratic(a, b, c, x):
    y = (a * x * x) + (b * x) + c
    return y


def common_part(val):
    print("Value of the function equals", val)
