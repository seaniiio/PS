def change(s):
    cnt_0 = 0
    for c in s:
        if c == '0':
            cnt_0 += 1
    result = bin(len(s) - cnt_0)
    return result[2:], cnt_0

def solution(s):
    answer = [0, 0]
    while s != "1":
        answer[0] += 1
        s, cnt = change(s)
        answer[1] += cnt
    return answer

# bin()을 이용하면 특정 숫자에 대한 이진 변환된 문자열을 얻을 수 있다.