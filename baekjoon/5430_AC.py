import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    function_l = list(input())
    n = int(input())

    l = input().rstrip()
    d = deque([])
    if l != '[]' :
        d = deque(list(map(int, l.lstrip('[').rstrip(']').split(','))))

    r = 1 # 1이면 popleft, -1이면 pop
    for f in function_l:
        if f == 'R':
            r *= (-1)
        elif f == 'D':
            if len(d) == 0:
                print('error')
                r = 0
                break
            if r == 1:
                d.popleft()
            elif r == -1:
                d.pop()

    if r != 0 and len(d) == 0:
        print('[]')
    elif r == 1:
        print('[', end='')
        for i in range(len(d)-1):
            print("{},".format(d[i]), end='')
        
        print('{}]'.format(d[len(d)-1]))
    elif r == -1:
        print('[', end='')
        for i in range(len(d)-1, 0, -1):
            print("{},".format(d[i]), end='')
        
        print('{}]'.format(d[0]))
