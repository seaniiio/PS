# 시간복잡도를 줄일 수 있는 딕셔너리 이용하기
# import sys

# N, M = map(int, sys.stdin.readline().split())
# count = 0
# no_listen = {}
# no_listen_no_see = {}

# for i in range(N):
#     no_listen_name = input()
#     no_listen[no_listen_name] = 'no_listen'
# for j in range(M):
#     no_see_name = input()
#     if no_see_name in no_listen:
#         count += 1
#         no_listen_no_see[no_see_name] = 'no_listen_no_see'

# sorted_list = sorted(no_listen_no_see.items())
# print(count)
# for t in sorted_list:
#     print(t[0])

# set 활용하기

import sys

N, M = map(int, sys.stdin.readline().split())
d = []
b = []

for i in range(N):
    n = input()
    d.append(n)
for j in range(M):
    n = input()
    b.append(n)

db = sorted(list(set(d) & set(b)))

print(len(db))
for k in db:
    print(k)
