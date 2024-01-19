# dp문제인거 기억 어렵다

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
dp[0][0][0] = 1
for i in range(21):
    dp[i][i][i] = 2 ** i

def w(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    if x > 20 or y > 20 or z > 20:
        return dp[20][20][20]
    if dp[x][y][z] != 0:
        return dp[x][y][z]
    if x < y and y < z:
        dp[x][y][z] = w(x, y, z-1) + w(x, y-1, z-1) - w(x, y-1, z)
    else:
        dp[x][y][z] = w(x-1, y, z) + w(x-1, y-1, z) + w(x-1, y, z-1) - w(x-1, y-1, z-1)
    return dp[x][y][z]
    
while True:
    x, y, z = map(int, input().split())
    if x == -1 and  y == -1 and z == -1:
        break
    print("w({}, {}, {}) = {}".format(x, y, z, w(x, y, z)))