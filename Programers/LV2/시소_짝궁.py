import math

def solution(weights):
    answer = 0
    weights.sort()
    weight_dict = {}
    for w in weights:
        if w in weight_dict:
            weight_dict[w] += 1
        else:
            weight_dict[w] = 1
    for w in weight_dict.values():
        if w > 1:
            answer += math.comb(w, 2)
            
    for w in weights:
        for a, b in (3, 2), (4, 3), (2, 1):
            if w % b == 0:
                if int(w * (a / b)) in weight_dict:
                    answer += weight_dict[int(w * (a / b))]
    return answer