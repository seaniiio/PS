from collections import deque
import itertools

n, m = map(int, (input().split()))
G = []
chic = []
house = []
for i in range(n):
    G.append(list(map(int, input().split())))
    for j in range(n):
        if G[i][j] == 2:
            chic.append([i, j])
        if G[i][j] == 1:
            house.append([i, j])

def chic_dist(l):
    total_cnt = 0
    for h in house:
        x, y = h
        temp_min = 2500
        for a, b in l:
            temp_min = min(temp_min, abs(a-x) + abs(b-y))
        total_cnt += temp_min
    return total_cnt
                    
min_v = 2500
for l in itertools.combinations(chic, m): # 폐업x
    min_v = min(chic_dist(l), min_v)

print(min_v)