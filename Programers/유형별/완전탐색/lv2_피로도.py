# 각 던전별로 리스트에 [탐험하기 위한 피로도, 탐험해서 소모되는 피로도]를 원소로 가진다.
# 한 유저의 현재 피로도가 주어졌을때, 유저가 탐험할 수 있는 최대 던전 수를 return

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    dungeons_p = permutations(dungeons, len(dungeons))
    for p in dungeons_p:
        piro = k
        dungeon_count = 0
        for d in p:
            if d[0] <= piro:
                dungeon_count += 1
                piro -= d[1]
        if dungeon_count > answer:
            answer = dungeon_count
    return answer