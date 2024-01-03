# 1
def solution(participant, completion):
    p_dict = {}
    for p in participant:
        if p in p_dict.keys():
            p_dict[p] = p_dict[p] + 1
        else:
            p_dict[p] = 1
    
    for c in completion:
        p_dict[c] = p_dict[c] - 1
        if p_dict[c] == 0:
            p_dict.pop(c)
    
    return list(p_dict.keys())[0]


# 2
def solution(participant, completion):
    hash_t = {}
    hash_sum = 0
    for p in participant:
        hash_t[hash(p)] = p
        hash_sum = hash_sum + hash(p)
    
    for c in completion:
        hash_sum = hash_sum - hash(c)
    return hash_t[hash_sum]