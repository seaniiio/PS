# 피보나치 -> DP

import sys

fibonacci = [[0, 1, 0], [1, 0, 1]]

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if len(fibonacci) <= n:
            f = fibo(n-1) + fibo(n-2)
            fibonacci.append([f])
        n0 = fibonacci[n-1][1] + fibonacci[n-2][1]
        n1 = fibonacci[n-1][2] + fibonacci[n-2][2]
        fibonacci[n].append(n0)
        fibonacci[n].append(n1)
        return fibonacci[n][0]

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    fibo(n)
    print(fibonacci[n][1], fibonacci[n][2])



