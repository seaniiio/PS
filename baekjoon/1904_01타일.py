n = int(input())
fib = [1] * 1000001
for i in range(2, n + 1):
    fib[i] = (fib[i-1] + fib[i-2]) % 15746
print(fib[n])