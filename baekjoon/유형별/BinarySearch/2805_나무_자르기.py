n, m = map(int, input().split())
tree = list(map(int, input().split()))

st, en = 1, max(tree)
while st <= en:
    mid = (st + en) // 2
    if sum(list(t - mid for t in tree if t > mid)) >= m:
        st = mid + 1
    else:
        en = mid - 1

print(en)