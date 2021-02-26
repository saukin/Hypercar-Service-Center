tag = "#"
inpt = int(input())

nElems = inpt * 2 - 1

for x in range(1, inpt + 1):
    print(("#" * (x * 2 - 1)).center(nElems))
