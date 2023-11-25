import sys
from collections import deque

N = int(sys.stdin.readline())
stack = deque()

for i in range(N):
    com = sys.stdin.readline().rstrip()
    if com[0] == '1':
        num = int(com.split()[-1])
        stack.append(num)
    elif com == '2':
        if len(stack) != 0: 
            print(stack.pop())
        else: print(-1)
    elif com == '3':
        print(len(stack))
    elif com == '4':
        if len(stack) == 0: print(1)
        else: print(0)
    elif com == '5':
        if len(stack) != 0: print(stack[len(stack) - 1])
        else: print(-1)

# sys를 사용해서 입력받자...
# input() 했다가 시간초과 났다