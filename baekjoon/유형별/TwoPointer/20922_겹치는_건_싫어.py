from collections import deque
n, k = map(int, input().split())
l = list(map(int, input().split()))

num = {i : 0 for i in range(1, 100001)}
max_l = 0
q = deque([])
for i in range(len(l)):
    q.append(l[i])
    num[l[i]] += 1
    if num[l[i]] > k:
        while True:
            e = q.popleft()
            num[e] -= 1
            if e == l[i]:
                break
    max_l = max(max_l, len(q))

print(max_l)
