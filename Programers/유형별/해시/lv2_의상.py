def solution(clothes):
    answer = 1
    cloth_dict = {}
    for cloth in clothes:
        if cloth[1] in cloth_dict:
            cloth_dict[cloth[1]].append(cloth[0])
        else:
            cloth_dict[cloth[1]] = ["not_wear", cloth[0]]
    for i in list(cloth_dict.values()):
        answer = answer * len(i)
    return answer - 1