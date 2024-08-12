# 1부터 쭉 더해서 N보다 커지면 거기서 빼기
# N > x(x+1) / 2 만족하는 최소 x 구하기
# x < (2*N + 1/4)^(1/2) - 1/2
import math

n = int(input())
x = math.ceil((2 * n + 1/4) ** 0.5 - 1/2)

s = (x * (x+1)) / 2
answer = x
if s != n:
    answer -= 1

print(answer)