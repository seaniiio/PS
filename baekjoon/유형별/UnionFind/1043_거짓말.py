# 유니온파인드

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
know_lie = set(map(int, input().split()[1:]))

party = []
for _ in range(m):
    party.append(set(map(int, input().split()[1:])))

know_lie = set(know_lie)
for _ in range(m):
    for p in party:
        if p & know_lie:
            know_lie = know_lie.union(p)

ans = 0
for p in party:
    if not p & know_lie:
        ans += 1

print(ans)