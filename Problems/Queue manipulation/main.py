from _collections import deque

queue = deque()

n = int(input())

for _i in range(n):
    inp = input().split(" ")
    if inp[0] == "ENQUEUE":
        queue.appendleft(inp[1])
    else:
        queue.pop()

while queue > 0:
    print(queue.pop())
