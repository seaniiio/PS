import sys

def round_f(n):
    return int(n + 0.5)

n = int(input())
x = round_f(n * 0.15)
lv = []
for _ in range(n):
    lv.append(int(sys.stdin.readline()))
lv.sort()

if n == 0:
    print(0)
else:
    lv_new = lv[x:n-x]
    result = round_f(sum(lv_new) / (n - 2 * x))
    print(result)