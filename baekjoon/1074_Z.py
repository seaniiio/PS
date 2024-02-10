N, r, c = map(int, input().split())
n = 2 ** N
answer = 0
n_x, n_y = 0, 0
while True:
    k = n // 2
    d = int(k ** 0.5)
    i = 0
    for x, y in ([0, k], [0, k]), ([0, k], [k, 2 * k]), ([k, k * 2], [0, k]), ([k, k * 2], [k, k * 2]):
        if n_x + x[0] <= r < n_x + x[1] and n_y + y[0] <= c < n_y + y[1]:
            N -= 1
            answer += i * (4 ** N)
            n //= 2
            n_x += x[0]
            n_y += y[0]
        i += 1
    if k == 1:
        break
print(answer)