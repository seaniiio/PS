n = int(input())
G = []
for _ in range(n):
    G.append(list(map(int, input().split())))

result = [0, 0]
def F(n, x, y):
    k = G[x][y]
    for i in range(n):
        for j in range(n):
            if G[x+i][y+j] != k:
                dn = int(n/2)
                for dx, dy in (x,y), (x+dn, y), (x, y+dn), (x+dn, y+dn):
                    F(dn, dx, dy)
                return
    result[k] += 1
F(n, 0, 0)
print(result[0])
print(result[1])