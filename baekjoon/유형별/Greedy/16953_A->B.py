a, b = map(int, input().split())

cnt = 0
while True:
    if a == b:
        cnt += 1
        break
    elif (b % 2 != 0 and b % 10 != 1) or a > b:
        cnt = -1
        break
    elif b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    cnt += 1

print(cnt)