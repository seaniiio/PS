# 해시테이블
N, M = map(int, input().split())

dict = {}
count = 0
for i in range(N):
    key = input()
    dict[key] = 1
for j in range(M):
    s = input()
    if s in dict:
        count += 1

print(count)