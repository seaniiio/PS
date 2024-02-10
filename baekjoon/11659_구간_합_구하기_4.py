import sys

n, m = map(int, input().split())
l = list(map(int, input().split()))

acum = 0
l2 = [0] * (n + 1)
for i in range(0, n):
    acum += l[i]
    l2[i+1] = acum

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(l2[j] - l2[i - 1])