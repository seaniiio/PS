n = int(input())

dp = {0 : 0, 1 : 1, 2 : 1}

def fibo(n):
    if n in dp.keys():
        return dp[n]
    
    if n % 2 == 0:
        a = fibo(n // 2)
        b = fibo(n // 2 - 1)
        dp[n] = (a * (a + 2*b)) % 1000000007
        return dp[n] 

    elif n % 2 == 1:
        a = fibo(n // 2)
        b = fibo(n // 2 + 1)
        dp[n] = (a ** 2 + b ** 2) % 1000000007
        return dp[n]

print(fibo(n))