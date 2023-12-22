def solution(s):
    time_x = 0
    time_not_x = 0
    answer = 0
    i = 0
    x = s[0]
    while True:
        if x == s[i]:
            time_x += 1
        else:
            time_not_x += 1
        if time_x != time_not_x and i == len(s) - 1:
            answer += 1
            break
        elif time_x == time_not_x:
            answer += 1
            if i == len(s) - 1:
                break
            s = s[i+1:]
            x = s[0]
            i = 0
            continue 
        i += 1
    return answer