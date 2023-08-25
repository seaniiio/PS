import sys

n = int(input())
arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))

arr1.sort()
arr2.sort()
sum = 0

for i in range(n):
    sum += arr1[i] * arr2[n-i-1]
print(sum)