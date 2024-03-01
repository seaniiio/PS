# L, R 연산을 str으로 바꿔서 deque 사용하고 join -> int -> return해줬더니 시간초과

from collections import deque
import sys

input = sys.stdin.readline

def D(n):
    return (n * 2) % 10000
def S(n):
    return n-1 if n != 0 else 9999
def L(n):
    return (n // 1000) + (n % 1000) * 10
def R(n):
    return (n // 10) + (n % 10) * 1000

def bfs(a, b):
    q = deque([[a, '']]) # 현재숫자, 현재명령어
    visited = [False] * 10001
    visited[a] = True
    while q:
        n, now = q.popleft()
        if n == b:
            return now
        for c, k in ('D', D(n)), ('S', S(n)), ('L', L(n)), ('R', R(n)):
            if visited[k] == False:
                visited[k] = True
                q.append([k, now + c])

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b))