def solution(msg):
    answer = []
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = {a : i+1 for i, a in enumerate(alpha)}
    max_num = 26
    i, next = 0, 1
    while i < len(msg):
        num = dic[msg[i]]
        while next <= len(msg) - 1 and msg[i:next+1] in dic:
            num = dic[msg[i:next+1]]
            next += 1
        # if next != len(msg) - 1:
        max_num += 1
        dic[msg[i:next+1]] = max_num
        answer.append(num)
        i = next
    return answer