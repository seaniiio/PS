n = int(input())
L = []
for _ in range(n):
    s = input().split()
    print(s)
    L.append((s[0], int(s[1])))

L.sort(key = lambda x:x[1])
for s in L:
    print(s[0], end=' ')