def solution(k, m, score):
    answer = 0
    total_apple = len(score)
    score.sort(reverse = True)
    i = 0
    while i + m <= total_apple:
        answer += ( m * score[i + m - 1])
        i += m
    return answer