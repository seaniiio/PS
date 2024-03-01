import sys
input = sys.stdin.readline

def maxi(n, m): # 최대공약수
    min_v = min(n, m)
    for k in range(min_v, 0, -1):
        if n % k == 0 and m % k == 0:
            return k

def mini(n, m): # 최소공배수
    return (n * m) // maxi(n, m)

t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    range_max = mini(n, m)
    result = -1
    for i in range(range_max // n):
        t = n * i + x
        if t % m == y:
            result = t
        elif t % m == 0 and y == m:
            result = t
    print(result)
