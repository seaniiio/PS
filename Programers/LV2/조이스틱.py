# greedy

def change_alpha(alpha):
    forward_dir = abs(ord('A') - ord(alpha))
    backward_dir = abs(ord('Z') - ord(alpha)) + 1 # 'z'로 바꾸는 1회
    return min(forward_dir, backward_dir)
    
def solution(name):
    name = list(name)
    total_move = 0
    min_move = len(name) - 1
    for i, n in enumerate(name):
        total_move += change_alpha(n)
        next = i+1
        while next < len(name) and name[next] == 'A':
            next += 1
        min_move = min(min_move, i * 2 + len(name) - next, 2 * (len(name) - next) + i)
        
    total_move += min_move
    return total_move