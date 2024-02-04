n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
test = list(map(int, input().split()))

def BS(k):
    st, en = 0, n-1
    while st <= en:
        mid = (st + en) // 2
        if arr[mid] == k:
            return 1
        elif arr[mid] < k:
            st = mid + 1
        elif arr[mid] > k:
            en = mid - 1
    return 0

for k in test:
    print(BS(k))