# nCk

fact = [1] * 1001

n, k = map(int, input().split())
for i in range(1, n+1):
    fact[i] = (fact[i-1] * i)

print(fact[:20])

print((fact[n]//(fact[n-k] * fact[k])) % 10007)