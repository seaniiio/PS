from collections import Counter

r, c, k = map(int,input().split())
r -= 1
c -= 1
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

time = 0

def new_sort(a):
    counter = Counter(a)
    sorting_a = []
    for k, v in counter.items():
        if k != 0:
            sorting_a.append((k,v))
    sorting_a.sort(key = lambda x: (x[1], x[0])) # (등장횟수, 수)

    new_a = []
    for s in sorting_a:
        new_a.extend([s[0], s[1]])
    return new_a

def sort_RC(rc):
    global A
    if rc == 'C':
        A = list(zip(*A))
    max_len = 0
    for i in range(len(A)):
        A[i] = new_sort(A[i])
        max_len = max(max_len, len(A[i]))
    
    for i in range(len(A)):
        if len(A[i]) <= max_len:
            A[i].extend([0] * (max_len - len(A[i])))
        if len(A[i]) > 100:
            A[i] = A[i][:100]
    
    if rc == 'C':
        A = list(zip(*A))

while True:
    if r < len(A) and c < len(A[0]) and A[r][c] == k:
        break
    if time == 100:
        time = -1
        break
    time += 1
    if len(A) >= len(A[0]): # R 연산
        sort_RC('R')
    else: # C 연산
        sort_RC('C')
  
print(time)