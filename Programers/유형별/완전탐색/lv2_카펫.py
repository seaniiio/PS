# 노란색과 갈색 카펫의 수만 주어진다.
# 카펫의 가로, 세로를 담아서 return해야 함
# 카펫의 가로길이 >= 세로길이

def solution(brown, yellow):
    answer = []
    brown_sum = brown // 2
    for i in range(1, brown_sum):
        answer = [brown_sum - i + 1, i + 1]
        if answer[0] * answer[1] - brown == yellow:
            break
    return answer