from collections import deque

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    ptr, cnt = 0, 1
    q = deque(map(int, input().split()))
    while True:
        if ptr == k and max(q) == q[ptr]:
            print(cnt)
            break
        elif max(q) == q[ptr]:
            q[ptr] = -1
            cnt += 1
        if ptr + 1 == n:
            ptr = 0
        else:
            ptr += 1