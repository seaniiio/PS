# 정수로 이루어진 리스트가 주어진다.
# 이 정수들을 이어붙여서 만들 수 있는 가장 큰 수를 return해야 한다.

def solution(numbers):
    answer = ""
    numbers_string = [str(i) for i in numbers]
    sorted_numbers = sorted(numbers_string, key = lambda x:x * 3, reverse=True) #  자릿수가 다른 정수를 제대로 정렬하는 방법
    for num in sorted_numbers:
        answer += num
    return str(int(answer))