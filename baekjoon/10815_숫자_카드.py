# set in연산 이용
n = int(input())
l = set(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
answer = [0 for _ in range(m)]
for i in range(m):
    print(int(find[i] in l), end=' ')


# 딕셔너리 key in연산 이용
dict = {}
n = int(input())
l = list(map(int, input().split()))
for k in l:
    dict[k] = True

m = int(input())
find = list(map(int, input().split()))
answer = [0 for _ in range(m)]
for i in range(m):
    if find[i] in dict.keys():
        answer[i] = 1

for a in answer:
    print(a, end=' ')