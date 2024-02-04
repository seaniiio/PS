import sys
k, n = map(int, sys.stdin.readline().split())
l = []
for _ in range(k):
    l.append(int(sys.stdin.readline()))

# upper bound
st, en = 1, sum(l) // n # st를 1로 설정해야 ZeroDivision 발생 안 함
while st <= en:
    mid = (st + en) // 2
    num = sum(list(i // mid for i in l))
    if num >= n: # 만족
        st = mid + 1
    else:
        en = mid - 1

print(en)