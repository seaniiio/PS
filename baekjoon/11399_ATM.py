import sys

n = int(input())
time = list(map(int, sys.stdin.readline().split()))

time.sort()
total_time = 0
for i in range(n):
    total_time += time[i] * (n - i)

print(total_time)