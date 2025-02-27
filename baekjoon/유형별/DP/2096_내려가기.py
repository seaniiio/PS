import sys
input = sys.stdin.readline

n = int(input())
g = []
g = list(map(int, input().split()))

dp_max, dp_min = g[:], g[:]
for i in range(n-1):

    g = list(map(int, input().split()))
    dp_max = [max(dp_max[0], dp_max[1]) + g[0], 
              max(dp_max[0], dp_max[1], dp_max[2]) + g[1], 
              max(dp_max[1], dp_max[2]) + g[2]]

    dp_min = [min(dp_min[0], dp_min[1]) + g[0],
                  min(dp_min[0], dp_min[1], dp_min[2]) + g[1],
                  min(dp_min[1], dp_min[2]) + g[2]]

print(max(dp_max), min(dp_min))