def solution(storey):
    answer = 0
    
    while storey > 0:
        now = storey % 10
        storey //= 10
        if now == 5:
            if storey % 10 >= 5:
                answer += (10 - now)
                storey += 1
            else:
                answer += now
        elif now >= 6:
            answer += (10 - now)
            storey += 1
        else:
            answer += now

    return answer