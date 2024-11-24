import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

n, m = map(int, input().split())
l = [i for i in range(n+1)]

def find(k):
    if l[k] != k:
        l[k] = find(l[k])
    return l[k]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        l[b] = a
    else:
        l[a] = b

for _ in range(m):
    t, a, b = map(int, input().split())
    if t == 0:
        union(a, b)

    else:
        if find(l[a]) == find(l[b]):
            print("YES")
        else:
            print("NO")