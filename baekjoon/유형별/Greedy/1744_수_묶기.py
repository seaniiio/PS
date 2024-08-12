# 그리디

# 0, (-), 1 신경쓰기
# (-) 여러개 있을 때 -> 절댓값 큰거부터 묶기, 남은거 있으면(홀수개일때) 0이랑 묶고, 0 없으면 그냥 냅두기
# 1은 무조건 안 묶고 그냥 더하는게 이득

n = int(input())
result = 0
nums_p, nums_n = [], []
for _ in range(n):
    n = int(input())
    if n == 1: 
        result += 1
    else:
        nums_p.append(n) if n > 0 else nums_n.append(n)

nums_p.sort(reverse=True)
nums_n.sort()

result += sum([nums_p[i] * nums_p[i+1] for i in range(len(nums_p) - 1) if (i % 2 == 0)])
result += nums_p[len(nums_p) - 1] if len(nums_p) % 2 == 1 else 0

result += sum([nums_n[i] * nums_n[i+1] for i in range(len(nums_n) - 1) if (i % 2 == 0)])
result += nums_n[len(nums_n) - 1] if len(nums_n) % 2 == 1 else 0

print(result)