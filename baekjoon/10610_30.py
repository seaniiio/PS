l = list(input())
l.sort(reverse=True)
int_l = []
for i, k in enumerate(l):
    int_l.append(int(k))
s = sum(int_l)

if s % 3 != 0 or int_l[-1] != 0:
    print(-1)
else:
    print(''.join(l))