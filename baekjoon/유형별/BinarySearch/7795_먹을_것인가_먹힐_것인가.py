# 전체탐색 X

t = int(input())
for _ in range(t):
    answer = 0
    n, m = map(int, input().split())
    a_l = list(map(int, input().split()))
    b_l = list(map(int, input().split()))
    a_l.sort()
    b_l.sort()
    for a in a_l: # 이분탐색
        st, en = 0, len(b_l)-1
        r = -1
        while st <= en:
            mid = (st + en) // 2
            if b_l[mid] < a:
                r = mid
                st = mid + 1
            else:
                en = mid - 1
        answer += (r+1)
    print(answer)
        