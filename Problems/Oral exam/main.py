from _collections import deque

READY = "READY"
EXTRA = "EXTRA"
PASSED = "PASSED"

queue = deque()
n = int(input())

for _i in range(n):
    inp = input().split(" ")
    if inp[0] == READY:
        queue.append(inp[1])
    elif inp[0] == EXTRA:
        queue.append(queue.popleft())
    elif inp[0] == PASSED:
        print(queue.popleft())
