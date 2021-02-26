# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
garden = dict.fromkeys(groups)

for x in range(int(input())):
    garden.update({groups[x]: int(input())})

print(garden)
