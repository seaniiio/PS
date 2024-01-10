# 컴퓨터들이 있고, 어떤 컴퓨터들은 서로 연결되어 있다.
# 이 때 네트워크의 수는?

from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            q = deque([i])
            answer += 1
            BFS(computers, visited, n, q)
    return answer

def BFS(computers, visited, n, q):
    i = q.popleft()
    for j in range(n):
        if j != i and visited[j] == False and computers[i][j] == 1:
            visited[j] = True
            q.append(j)
            BFS(computers, visited, n, q)
            
# DFS/BFS 문제
# 네트워크 안의 한 컴퓨터에서 BFS로 훑고 지나간 컴퓨터를 visited로 표시한다.
# 이후 BFS가 끝난 뒤 아직 visited가 False인 부분은 다른 네트워크이므로 이를 반복하면서 네트워크의 수를 센다.