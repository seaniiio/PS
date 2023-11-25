# dictionary

import sys

N, M = map(int, sys.stdin.readline().split())
poketmons = {}
poketmons2 = {}
for i in range(1, N+1):
    name = sys.stdin.readline().rstrip()
    i_str = str(i)
    poketmons[i_str] = name
    poketmons[name] = i_str
for j in range(M):
    quiz = sys.stdin.readline().rstrip()
    if quiz in poketmons:
        print(poketmons[quiz])
    elif quiz in poketmons2:
        print(poketmons2[quiz])
