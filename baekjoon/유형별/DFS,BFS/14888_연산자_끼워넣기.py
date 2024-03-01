n = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))
min = int(10e9+1)
max = int(-10e9-1)

def dfs(p, m, mul, div, now, i):
    global min, max
    if i == n:
        if now > max:
            max = now
        if now < min:
            min = now
        return
    if p:
        dfs(p-1, m, mul, div, now+num[i], i+1)
    if m:
        dfs(p, m-1, mul, div, now-num[i], i+1)
    if mul:
        dfs(p, m, mul-1, div, now*num[i], i+1)
    if div:
        if now < 0:
            dfs(p, m, mul, div-1, (-1 * ((-1 * now)//num[i])), i+1)
        else:
            dfs(p, m, mul, div-1, now//num[i], i+1)


dfs(oper[0], oper[1], oper[2], oper[3], num[0], 1)
print(max)
print(min)