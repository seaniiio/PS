import sys

n, m = map(int, sys.stdin.readline().split())
dict = {}
for i in range(n):
    site, pwd = sys.stdin.readline().split()
    dict[site] = pwd
for j in range(m):
    s = sys.stdin.readline().rstrip()
    print(dict[s])