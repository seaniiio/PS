import sys

t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    dict = {}
    for _ in range(n):
        a, b = sys.stdin.readline().split()
        if b in dict:
            dict[b] += 1
        else:
            dict[b] = 1
    result = 1
    for d in dict.values():
        result *= (d + 1)
    print(result - 1)
