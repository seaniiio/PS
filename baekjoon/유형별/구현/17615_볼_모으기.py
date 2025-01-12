N = int(input())
balls = list(input())
ans = N

for color in ("R", "B"):
    l_i = 0
    while l_i < N and balls[l_i] == color:
        l_i += 1
    cnt = 0
    for i in range(l_i, N):
        if balls[i] == color:
            cnt += 1
    ans = min(ans, cnt)


for color in ("R", "B"):
    r_i = N - 1
    while r_i >= 0 and balls[r_i] == color:
        r_i -= 1
    cnt = 0
    for i in range(r_i, -1, -1):
        if balls[i] == color:
            cnt += 1
    ans = min(ans, cnt)

print(ans)