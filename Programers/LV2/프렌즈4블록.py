def block_match(i, j, board):
    match = True
    b = board[i][j]
    if b == 'X':
        return False
    for di, dj in (i+1, j), (i, j+1), (i+1, j+1):
        if board[di][dj] != b:
            match = False
    return match
    
def block_down(i, j, board):
    next = i
    while next+1 < len(board) and board[next+1][j] == 'X':
        next += 1
    return next

def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]
    
    while True:
        is_match = []
        for i in range(m-1):
            for j in range(n-1):
                if block_match(i, j, board):
                    is_match.extend([(i, j), (i+1, j), (i, j+1), (i+1, j+1)])
                    
        is_match = list(set(is_match))
        if len(is_match) == 0:
            break
        answer += len(is_match)
        
        for i, j in is_match:
            board[i][j] = 'X'
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                next = block_down(i, j, board)
                if next != i: 
                    board[next][j] = board[i][j]
                    board[i][j] = 'X'
    return answer