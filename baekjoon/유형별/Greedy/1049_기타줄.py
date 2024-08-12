# 6개 vs 1개 줄당 가격 비교

n, m = map(int, input().split())
cost_six, cost_one = [], []
for _ in range(m):
    a, b = map(int, input().split())
    cost_six.append(a)
    cost_one.append(b)

cost_six.sort()
cost_one.sort()

answer = 0
if cost_one[0] < cost_six[0] / 6:
    answer = n * cost_one[0]
else:
    answer += (n // 6) * cost_six[0]
    answer += (n % 6) * cost_one[0] if (n % 6) * cost_one[0] < cost_six[0] else cost_six[0] # 낱개로 채우는거보다 6개묶음이 싼 경우

print(answer)