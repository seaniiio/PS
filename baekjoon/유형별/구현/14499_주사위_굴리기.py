
dice = [0, 0, 0, 0, 0, 0, 0]
def dice_roll(c):
    global dice
    if c == 1:
        dice = [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
    elif c == 2:
        dice = [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
    elif c == 3:
        dice = [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]
    else:
        dice = [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]

n, m, x, y, k = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

commands = list(map(int, input().split()))
move = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
for c in commands:
    dx, dy = x + move[c][0], y + move[c][1]
    if 0 <= dx < n and 0 <= dy < m:
        x, y = dx, dy
        dice_roll(c)
        if board[x][y] == 0:
            board[x][y] = dice[6]
        else:
            dice[6] = board[x][y]
            board[x][y] = 0

        print(dice[1])
