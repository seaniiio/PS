# n = 10^9, m= 3*10^5

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
jewels = []
for _ in range(m):
    jewels.append(int(input()))

jealousy = 0
jewels.sort(reverse=True)

st, en = 1, max(jewels)
ans = 0
while st <= en:
    mid = (st + en) // 2
    s = 0
    for j in jewels:
        s += (j // mid)
        if j % mid != 0:
            s += 1
    if s <= n:
        ans = mid
        en = mid - 1
    else:
        st = mid + 1
print(ans)