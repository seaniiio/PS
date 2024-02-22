# 소수 구하는 로직에서 범위 : range(2, (n ** 0.5))

from collections import deque

def change(n, k):
    r = deque([])
    while n // k > 0:
        r.appendleft(str(n % k))
        n //= k
    r.appendleft(str(n % k))
    return r

def spl(r):
    r = list(''.join(r).split('0'))
    while '' in r:
        r.remove('')
    return r

def is_prime(n):
    if n == 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
        
def solution(n, k):
    answer = 0
    r = change(n, k)
    new_r = spl(r)
    for k in new_r:
        if is_prime(int(k)):
            answer += 1
    return answer
