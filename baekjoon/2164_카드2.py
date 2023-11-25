# queue 문제
# list보다 시간초과가 적게 발생하는 deque 사용
from collections import deque

n = int(input())
queue = deque()
for i in range(n):
    queue.append(i+1)
count = 1

while(len(queue) != 1):
    if(count % 2 == 1):
        queue.popleft()
    else:
        k = queue[0]
        queue.popleft()
        queue.append(k)
    count += 1

print(queue[0])
