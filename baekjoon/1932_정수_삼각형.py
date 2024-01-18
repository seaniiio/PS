# n = int(input())
# G = []
# answer = 0
# for i in range(n):
#     G.append(list(map(int, input().split())))

# def DFS(depth, sum, idx):
#     if depth == n-1:
#         global answer
#         answer = max(answer, sum + G[n-1][idx])
#         return
#     DFS(depth + 1, sum + G[depth][idx], idx)
#     DFS(depth + 1, sum + G[depth][idx], idx + 1)

# DFS(0, 0, 0)
# print(answer)
# 시간 초과


# DP(구현..?)
n = int(input())
G = []
answer = 0
for i in range(n):
    G.append(list(map(int, input().split())))
for i in range(n-2, -1, -1):
    for j in range(i+1):
        G[i][j] = max(G[i+1][j], G[i+1][j+1]) + G[i][j]
print(G[0][0])
