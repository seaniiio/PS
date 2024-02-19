n = int(input())
l = [i for i in range(1, n+1)]
ptr = 0
for i in range(1, n):
    n = len(l)
    ptr += (i ** 3) - 1
    ptr %= n
    rem = l[ptr]
    l.remove(rem)
print(l[0])