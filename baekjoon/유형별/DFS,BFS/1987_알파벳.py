# 메모리초과?

# import sys
# input = sys.stdin.readline

# r, c = map(int, input().split())
# b = []
# for _ in range(r):
#     b.append(list(input().strip()))

# def move(i, j, visited):
#     moves = 1
#     initial_moves = 1
#     for di, dj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
#         if 0 <= di < r and 0 <= dj < c:
#             if visited[ord(b[di][dj]) - 65] == False:
#                 moves_temp = initial_moves
        
#                 new_visited = visited[:]
#                 new_visited[ord(b[di][dj]) - 65] = True

#                 moves_temp += move(di, dj, new_visited)
#                 moves = max(moves, moves_temp)

#     return moves

# visited = [False] * 26
# visited[ord(b[0][0]) - 65] = True
# print(move(0, 0, visited))


# 비트마스크로 visited 확인하기(메모리 초과 방지)

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
b = []
for _ in range(r):
    b.append(list(input().strip()))

def move(i, j, visited):
    moves = 1
    initial_moves = 1
    for di, dj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
        if 0 <= di < r and 0 <= dj < c:
            if not 1 << (ord(b[di][dj]) - 65) & visited:
                moves_temp = initial_moves
                moves_temp += move(di, dj, visited | (1 << (ord(b[di][dj]) - 65)))
                moves = max(moves, moves_temp)

    return moves

visited = 1 << (ord(b[0][0]) - 65)
print(move(0, 0, visited))
