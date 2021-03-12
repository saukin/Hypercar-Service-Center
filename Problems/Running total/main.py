_list = [int(x) for x in list(input())]

new_list = [sum(_list[:x + 1]) for x in range(len(_list))]

print(new_list)
