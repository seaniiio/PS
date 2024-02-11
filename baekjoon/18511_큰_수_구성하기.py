import itertools

n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
num_len = len(str(n)) # 3자리면 3
result = 0

for i in itertools.product(l, repeat=num_len):
    num = int(''.join(list(map(str, i))))
    if num <= n:
        result = max(result, num)

for i in itertools.product(l, repeat=num_len - 1):
    num = int(''.join(list(map(str, i))))
    if num <= n:
        result = max(result, num)

print(result)
