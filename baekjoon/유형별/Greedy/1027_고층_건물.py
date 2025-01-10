N = int(input())
l = list(map(int, input().split()))

max_t = 0
for i in range(N):
    t = 0
    for j in range(N):
        if i == j:
            continue
        visible = True
        if j < i: # 왼쪽의 건물
            a = (l[i] - l[j]) / abs(i - j)
            for k in range(j+1, i):
                if l[k] >= l[j] + a * (k - j): # 접하는 경우
                    visible = False
        
        elif j > i: # 뒷쪽의 건물
            a = (l[j] - l[i]) / abs(i - j)
            for k in range(i+1, j):
                if l[k] >= l[i] + a * (k - i):
                    visible = False
        
        if visible:
            t += 1
    max_t = max(max_t, t)

print(max_t)