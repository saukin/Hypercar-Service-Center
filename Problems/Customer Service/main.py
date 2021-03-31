from collections import deque

queue = deque()

n = int(input())

for _i in range(n):
    inp = input().split(" ")
    if inp[0] == "ISSUE":
        queue.appendleft(inp[1])
    else:
        queue.pop()

while len(queue) > 0:
    print(queue.pop())
