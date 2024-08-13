n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr = arr[::-1]
answer = 0

for i in range(n-1):
    max_v = max(arr[i+1:])

    for j in range(i+1, n):
        if arr[j] >= arr[i]:
            answer += (arr[j] - arr[i] + 1)
            arr[j] = arr[i] - 1

print(answer)

# n^2