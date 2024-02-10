import sys

n = int(input())
l = list(map(int, sys.stdin.readline().split()))

s = list(set(l))
s.sort()
dict = {}
for i, k in enumerate(s):
    dict[k] = i

for r in l:
    print(dict[r], end=' ')