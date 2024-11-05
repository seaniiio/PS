import sys
input = sys.stdin.readline

N = int(input())
students = []
students_locate = {i : [0, 0] for i in range(1, N ** 2+1)}
board = [[0] * N for _ in range(N)]

for _ in range(N ** 2):
    l = list(map(int, input().split()))
    students.append([l[0], l[1:]])

def locate(s, idx):
    global board
    seats = []
    for i in range(N):
        for j in range(N):
            like, blank = 0, 0
            if board[i][j] == 0:
                for di, dj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                    if 0 <= di < N and 0 <= dj < N:
                        if board[di][dj] == 0:
                            blank += 1
                        elif board[di][dj] in students[idx][1]:
                            like += 1
                seats.append([like, blank, i, j])
    
    seats.sort(key = lambda x:(x[0], x[1], -x[2], -x[3]), reverse=True)

    board[seats[0][2]][seats[0][3]] = s
    students_locate[s] = [seats[0][2], seats[0][3]]

for i, s in enumerate(students):
    locate(s[0], i)

score = {0 : 0, 1 : 1, 2 : 10, 3 : 100, 4 : 1000}
ans = 0
for s in students:
    i, j = students_locate[s[0]]
    like = 0
    for di, dj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
        if 0 <= di < N and 0 <= dj < N:
            if board[di][dj] in s[1]:
                like += 1
    ans += score[like]

print(ans)