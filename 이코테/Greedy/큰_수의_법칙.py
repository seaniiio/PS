# 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음

# 내 풀이
# import sys
# input = sys.stdin.readline

# n, m, k = map(int, input().split())
# l = list(map(int, input().split()))
# l.sort(reverse=True)

# cnt, sum = 0, 0

# for i in range(m):
#     if cnt == k:
#         sum += l[1]
#         cnt = 0
#     else:
#         sum += l[0]
#     cnt += 1
# print(sum)

# 이 문제를 해결하려면 일단 입력값 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 된다.
#  연속으로 더할 수 있는 횟수는 최대 K번이므로 ‘가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산’을 반복하면 된다.
# M의 크기가 100억 이상처럼 커진다면 시간 초과 판정을 받을 것이다.

# 반복되는 수열을 이용한 풀이

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)

first = l[0]
second = l[1]

# 가장 큰 수(first)가 더해지는 횟수
count = (m // k) * (k - 1) + (m % k)

sum = count * first + (m - count) * second
print(sum)
