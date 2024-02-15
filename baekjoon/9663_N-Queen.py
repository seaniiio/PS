n = int(input())
d = [0] * n
answer = 0

def possible(y):
    for i in range(y):
        if d[y] == d[i] or abs(y - i) == abs(d[y] - d[i]):
            return False
    return True


def f(y):
    global answer
    if y == n:
        answer += 1
        return

    for i in range(n):
        d[y] = i
        if possible(y):
            f(y+1)

f(0)
print(answer)