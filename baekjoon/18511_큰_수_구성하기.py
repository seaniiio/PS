# 재귀
n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.append(0)
nums.sort(reverse=True)
answer = 0
def rec(m, d):
    temp = m + nums[0] * (10 ** d)
    if temp < n:
        result = rec(temp, d+1)
        return result
    elif temp >= n:
        for num in nums:
            temp = m + num * (10 ** d)
            if temp <= n:
                return temp
print(rec(0, 0))