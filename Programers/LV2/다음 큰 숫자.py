def number_of_one(n):
    count = 1
    while n // 2 != 0:
        count += (n % 2)
        n //= 2
    count += (n % 2)
    return count

def solution(n):
    answer = 0
    target = number_of_one(n)
    print("target:", target)
    while True:
        n += 1
        if number_of_one(n) == target:
            answer = n
            break
    return answer