import sys

n = int(input())
s = set([])

for _ in range(n):
    l = list(sys.stdin.readline().split())
    if l[0] == 'all':
        s = set([i for i in range(1, 21)])
    elif l[0] == 'empty':
        s = set([])
    elif l[0] == 'add':
        s.add(int(l[1]))
    elif l[0] == 'remove':
        if int(l[1]) in s:
            s.remove(int(l[1]))
    elif l[0] == 'check':
        if int(l[1]) in s:
            print(1)
        else:
            print(0)
    elif l[0] == 'toggle':
        if int(l[1]) in s:
            s.remove(int(l[1]))
        else:
            s.add(int(l[1]))