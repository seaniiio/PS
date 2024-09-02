n = int(input())
L = []
for _ in range(n):
    L.append(int(input()))
L.sort(reverse=True)

for k in L:
    print(k, end=' ')