def gcd(a, b):
    g = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            g = i
    return g

def mcm(a, b):
    return (a * b) // gcd(a, b)

def solution(arr):
    answer = 1
    for i in range(len(arr)):
        answer = mcm(answer, arr[i])
    return answer