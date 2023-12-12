# players에 달리기 선수에 참여하는 선수들의 이름이 담겨있음
# callings에 추월한 선수의 목록이 담겨있음
# 최종 순위는?

def solution(players, callings):
    dict = {}
    for i in range(len(players)):
        dict[players[i]] = i + 1 # player : 순위
    for call in callings:
        dict[call] = dict[call] - 1 # 추월한 선수의 순위를 하나 낮춰준다.
        rank = dict[call]
        dict[players[rank-1]] = dict[players[rank-1]] + 1 # 추월당한 선수의 순위를 늘려준다.
        players[rank], players[rank - 1] = players[rank - 1], players[rank] # 실제 순위를 반영하여 swap해준다.
    return players