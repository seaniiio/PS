n, amount = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse = True)

cnt = 0
while amount != 0:
    for c in coin:
        while amount >= c:
            k = amount // c
            amount -= k * c
            cnt += k
print(cnt)