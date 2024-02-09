# 처음 생각한 방법
# 오른쪽 주유소부터, 왼쪽에 위치한 기름값이 min인 주유소에서 해당 거리만큼 충전한다고 하자
# 이 경우 O(^2/2) -> 5억 -> 시간초과 예상

# 두 번째 생각한 방법
# 왼쪽부터 탐색하면서, global min값을 저장해놓자ss
# min_list = []해서, index별로 해당 위치의 주유소까지 최소값을 구하자.

import sys

n = int(sys.stdin.readline())
dist_list = list(map(int, sys.stdin.readline().split()))
end_list = list(map(int, sys.stdin.readline().split()))

min_v = end_list[0]
min_list = [end_list[0]] * n
for i in range(1, n):
    if min_v > end_list[i]:
        min_v = end_list[i]
    min_list[i] = min_v

print(sum(list(i * j for i, j in zip(min_list, dist_list))))
