n, k = map(int, input().split())
s = n - (k * (k + 1)) / 2

result = 0
if s < 0:
    result = -1
else:
    result = k - 1 if s % k == 0 else k
print(result)