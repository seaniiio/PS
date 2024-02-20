import sys
top = [0, 0, 0, 0, 0]
T = [[0, 0, 0, 0, 0, 0, 0, 0]]
for _ in range(4):
    T.append(list(map(int, list(sys.stdin.readline().rstrip()))))

def right(i):
    return T[i][(top[i] + 2) % 8]

def left(i):
    return T[i][(top[i] + 6) % 8]

def cir(i, d):
    top[i] += (d * (-1))
    if top[i] < 0:
        top[i] = 7
    elif top[i] >= 8:
        top[i] = 0

def f(i, d, visited):
    visited[i] = True
    if i > 1:
        if right(i-1) != left(i) and visited[i-1] == False:
            f(i-1, (-1)*d, visited)
    if i < 4:
        if right(i) != left(i+1) and visited[i+1] == False:
            f(i+1, (-1)*d, visited)
    cir(i, d)

def cal(top):
    res = 0
    for i in range(1, 5):
        res += T[i][top[i]] * (2 ** (i-1))
    return res

t = int(input())
for _ in range(t):
    visited = [False, False, False, False, False]
    i, d = map(int, sys.stdin.readline().split())
    f(i, d, visited)
print(cal(top))