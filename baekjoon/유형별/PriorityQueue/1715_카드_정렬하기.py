import sys
from queue import PriorityQueue

input = sys.stdin.readline
n = int(input())
q = PriorityQueue()

for _ in range(n):
    q.put(int(input()))

result = 0

if n != 1:
    while not q.empty():
        q1 = q.get()
        q2 = q.get()
        s = q1 + q2
        result += (s)
        if q.empty():
            break
        q.put(s)

print(result)