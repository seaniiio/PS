n = int(input())
a = list(map(int, input().split()))
total = int(input())

st, en = 1, max(a)
while st <= en:
    mid = (st + en) // 2
    if sum(list(map(lambda x: x if x <= mid else mid, a))) <= total:
        st = mid + 1
    else:
        en = mid - 1
print(en)