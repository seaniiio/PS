# 인접한 학생끼리의 키 차이를 저장
# 차이가 큰 것부터 K개만큼 뺌

n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

costs = [h[i+1] - h[i] for i in range(0, n-1)]
costs.sort(reverse=True)
total_costs = sum(costs)

for i in range(k-1):
    total_costs -= costs[i]

print(total_costs)