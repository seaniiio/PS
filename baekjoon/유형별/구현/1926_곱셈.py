a, b, c = map(int, input().split())

def solution(a, b, c):
    if b == 1:
        return a % c
    
    temp = solution(a, b // 2, c)
    if b % 2 == 1:
        return ((temp * temp) % c) * a % c
    return ((temp * temp)) % c

print(solution(a, b, c))