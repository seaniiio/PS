# 해시 풀이
import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(input())
    l1 = list(map(int, sys.stdin.readline().split()))
    d = {k:0 for k in l1}
    m = int(input())
    l2 = list(map(int, sys.stdin.readline().split()))

    for k in l2:
        if k in d.keys():
            print(1)
        else:
            print(0)

# 이분탐색 풀이
# import sys
# t = int(sys.stdin.readline())

# for _ in range(t):
#     n = int(input())
#     l1 = list(map(int, sys.stdin.readline().split()))
#     m = int(input())
#     l2 = list(map(int, sys.stdin.readline().split()))

#     l1.sort()
#     for k in l2:
#         st, en = 0, n-1
#         answer = 0
#         while st <= en:
#             mid = (st + en) // 2
#             if l1[mid] == k:
#                 answer = 1
#                 break
#             elif l1[mid] > k:
#                 en = mid - 1
#             elif l1[mid] < k:
#                 st = mid + 1
#         print(answer)
