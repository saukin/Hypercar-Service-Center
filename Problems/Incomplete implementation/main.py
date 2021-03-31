def startswith_capital_counter(names):
    count = 0
    for name in names:
        if name.istitle():
            count += 1

    return count

# a = "Dfsf"
# print(a[0].isupper())
