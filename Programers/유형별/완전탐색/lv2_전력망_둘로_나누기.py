# 트리형태로 연결되어 있는 송전탑이 주어짐
# 하나의 전선을 끊었을 때, 두 전력망의 송전탑 개수 차이의 최솟값 구하기

import copy

def solution(n, wires):
    answer = 101
    for i in range(len(wires)):
        disconnected_wires = copy.deepcopy(wires) 
        disconnected_wires.remove(wires[i]) # 특정 송전탑 사이의 연결을 끊는다 → 그 요소를 없애면 됨
        visited = [False] * 101
        A_net = DFS(wires[i][0], disconnected_wires, visited)
        B_net = DFS(wires[i][1], disconnected_wires, visited)
        if answer > abs(A_net - B_net):
            answer = abs(A_net - B_net)
    return answer

def DFS(n, l, visited):
    net_num = 1
    visited[n] = True # 방문 표시
    for k in l:
        if k[0] == n and visited[k[1]] == False:     
            net_num += DFS(k[1], l, visited)              
        elif k[1] == n and visited[k[0]] == False:
            net_num += DFS(k[0], l, visited)
    return net_num