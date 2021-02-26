# put your python code here
seq = input().split()
num = input()
out = []

for x in enumerate(seq):
    if x[1] == num:
        out.append(str(x[0]))

if len(out) == 0:
    print("not found")
else:
    print(" ".join(out))
