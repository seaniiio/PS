def solution(s):
    word_list = list(s)
    for idx, c in enumerate(word_list):
        if idx == 0:
            word_list[idx] = c.upper()
        elif word_list[idx-1] == ' ':
            word_list[idx] = c.upper()
        else:
            word_list[idx] = c.lower()
    answer = ''.join(word_list) 
    return answer

# enumerate를 활용하면, 리스트의 인덱스와 요소 모두 활용할 수 있다.
# 공백이 중복으로 주어질 수 있다 → 바로 이전의 글자가 공백일 경우, upper를 해준다
# 바로 이전의 글자가 공백이 아닌 경우, lower를 해준다.