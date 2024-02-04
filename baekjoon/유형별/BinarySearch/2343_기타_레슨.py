n, m = map(int, input().split())
a = list(map(int, input().split()))

def search(limit):
    cnt, sum = 0, 0
    for ptr in range(0, n):
        if sum + a[ptr] > limit:
            cnt += 1
            sum = a[ptr]
        else:
            sum += a[ptr]
    if sum:
        cnt += 1
    if cnt <= m:
        return True
    return False


st, en = max(a), sum(a)
answer = 0
while st <= en:
    mid = (st + en) // 2
    if search(mid) == True:
        en = mid - 1
    else:
        st = mid + 1
print(st)
