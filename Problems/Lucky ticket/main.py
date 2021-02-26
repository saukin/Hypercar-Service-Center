# Save the input in this variable
ticket = input()

# Add up the digits for each half
half1 = 0
for x in range(3):
    half1 += int(ticket[x])
half2 = 0
for x in range(1, 4, 1):
    half2 += int(ticket[-x])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
