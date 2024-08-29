import sys
sys.setrecursionlimit(10**6)

n = int(input())
tanghuru = list(map(int, input().split()))
max_len = 1
fruits = {i : 0 for i in range(1, 10)}

def fruit(st, en, kind):
    global max_len

    max_len = max(max_len, en - st + 1)
    if en == n-1:
        return
    
    if fruits[tanghuru[en+1]] == 0:
        if kind == 2:
            if fruits[tanghuru[st]] == 1:
                kind -= 1
            fruits[tanghuru[st]] -= 1
            st += 1
        else:
            en += 1
            fruits[tanghuru[en]] = 1
            kind += 1
    else:
        en += 1
        fruits[tanghuru[en]] += 1
    
    fruit(st, en, kind)

fruits[tanghuru[0]] = 1
fruit(0, 0, 1)
print(max_len)