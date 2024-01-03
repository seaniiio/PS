# 숫자로 이루어진 문자열이 주어진다.
# 각 숫자로 만들 수 있는 수 중에서 소수인 수의 개수를 return한다.

from itertools import permutations

def solution(numbers):
    answer = 0
    numbers_permutations = []
    for i in range(1, len(numbers) + 1):
        numbers_permutations.extend(permutations(numbers, i))
    numbers_list = [int(''.join(p)) for p in numbers_permutations]
    numbers_list = list(set(numbers_list))
    for num in numbers_list:
        if isPrime(num):
            answer += 1
    return answer

def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True