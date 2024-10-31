import sys
input = sys.stdin.readline

N, L = map(int, input().split())
row = []
for _ in range(N):
    row.append(list(map(int, input().split())))
col = list(zip(*row))

def checkRoad(road):
    visited = [False] * N
    for i in range(N-1):
        now = road[i]
        next = road[i+1]
        if now != next: # 높이 바뀜
            if abs(now - next) >= 2:
                return False
            
            if now == next + 1:
                for j in range(1, L+1):
                    if i + j >= N or road[i + j] != next or visited[i + j]:
                        return False
                    visited[i + j] = True

            if now == next - 1:
                for j in range(L):
                    if i - j < 0 or road[i - j] != now or visited[i - j]:
                        return False
                    visited[i - j] = True

    return True

answer = 0
for i in range(N):
    if checkRoad(row[i]):
        answer += 1
    if checkRoad(col[i]):
        answer += 1

print(answer)