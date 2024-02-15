import itertools

n = int(input())
G = []
for _ in range(n):
    G.append(list(map(int, input().split())))

players = [i for i in range(n)]
def f(a):
    b = list(set(players) - set(a))
    score_a, score_b = 0, 0
    for i in a:
        for j in a:
            score_a += G[i][j]
    for i in b:
        for j in b:
            score_b += G[i][j]
    return abs(score_a - score_b)

cnt = 0
min_v = 100000
for l in itertools.combinations(players, n // 2):
    min_v = min(f(l), min_v)
print(min_v)