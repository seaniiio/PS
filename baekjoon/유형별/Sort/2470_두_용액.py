n = int(input())
L = list(map(int, input().split()))
acid, alkali = [], []
for k in L:
    if k < 0:
        alkali.append(k)
    else:
        acid.append(k)

acid.sort()
alkali.sort(reverse=True)

min_v = 2 * (10 ** 9) + 1
x = [0, 0]
# 한 종류만 혼합했을 때가 최소일 때
if len(acid) >= 2:
    if abs(acid[0] + acid[1]) < min_v:
        min_v = acid[0] + acid[1]
        x[0], x[1] = acid[0], acid[1]
if len(alkali) >= 2:
    if abs(alkali[0] + alkali[1]) < min_v:
        min_v = abs(alkali[0] + alkali[1])
        x[0], x[1] = alkali[0], alkali[1]

# 두개를 혼합한 경우가 최소일 때
if len(acid) > 0 and len(alkali) > 0:
    acid_idx, alkali_idx = 0, 0
    while True:
        s = acid[acid_idx] + alkali[alkali_idx]
        if min_v > abs(s):
            min_v = abs(s)
            x[0], x[1] = alkali[alkali_idx], acid[acid_idx]
        if s < 0: # 알칼리성이 센 경우 -> 산성 높이기
            if acid_idx == len(acid) - 1:
                break
            acid_idx += 1
        else:
            if alkali_idx == len(alkali) - 1:
                break
            alkali_idx += 1

x.sort()
print(x[0], x[1])