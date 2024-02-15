# from collections import deque

# n = int(input())
# q = deque([[0, 0], [1, 0], [2, 0]]) # 사자 어디에, y축
# cnt = 0

# while q:
#     x, y = q.popleft()
#     if y == n - 1:
#         cnt += 1
#         continue
#     for dx, dy in (0, y+1), (1, y+1), (2, y+1):
#         if x == 0: # 이전칸에 사자가 없음
#             q.append([dx, dy])
#         else: # 사자 있음
#             if x != dx:
#                 q.append([dx, dy])

# print(cnt)

n = int(input())
dp = [[1, 1, 1] for _ in range(n+1)]
for i in range(1, n):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901
print(sum(dp[n-1]) % 9901)