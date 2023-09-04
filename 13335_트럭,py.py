from collections import deque

n, w, l = map(int, input().split())
q = deque(map(int, input().split()))

sec = 0
now_kg = 0

while len(q) != 0:
    truck = q[0]
    
