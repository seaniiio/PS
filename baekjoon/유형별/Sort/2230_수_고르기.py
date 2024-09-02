# left, right index 이용
# L[left] + L[right]가 M보다 작으면 차이를 늘려야함 ->  right += 1, K보다 크면 차이를 줄여야 함 -> left += 1

n, m = map(int, input().split())
L = []
for _ in range(n):
    L.append(int(input()))

L.sort()
left, right = 0, 0
min_v = 2 * (10 ** 9) + 1
while left <= right and right <= n-1:
    sum_v = abs(L[left] - L[right])
    if m <= sum_v < min_v:
        min_v = sum_v
    if m <= sum_v:
        left += 1
    elif m > sum_v:
        right += 1

print(min_v)