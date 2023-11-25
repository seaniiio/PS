# 해싱
# "abba" -> 1 2 2 1
# 충돌을 줄이기 위해 계수 부여
# r = 31, M = 1234567891

import sys

L = int(sys.stdin.readline())
key = sys.stdin.readline()
r = 31
M = 1234567891
hash_value = 0

for i in range(L):
    hash_value += (ord(key[i]) - ord('a') + 1) * (r ** i)

hash_value %= M
print(hash_value)
