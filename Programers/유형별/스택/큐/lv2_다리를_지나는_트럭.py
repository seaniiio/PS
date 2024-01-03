from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    now_weight = 0 # 다리위의 트럭 weight 합
    on_bridge = deque() # 다리위에 있는 트럭 queue

    while len(truck_weights):
        s = sum([i[0] for i in on_bridge]) # 현재 다리 위의 트럭의 무게 합
        if s + truck_weights[0] <= weight: # 다음 트럭이 올라갈 수 있는 상황이면
            t = truck_weights.popleft() # 대기중인 트럭에서 첫번째 트럭을 빼서
            on_bridge.append([t, bridge_length]) # 다리 위에 올림 [트럭 무게, 남은 거리]
        answer = answer + 1 # 1초 경과
        for o in on_bridge:
            o[1] = o[1] - 1 # 1초 경과했으므로 다리 위의 모든 트럭의 남은 거리에서 1씩 빼줌
        if on_bridge[0][1] == 0: # 다리를 다 지났으면
            on_bridge.popleft() # 다리 위의 트럭 queue에서 pop
    return answer + bridge_length # 마지막 트럭이 출발하면서 while문이 끝나기 때문에 마지막 트럭이 건너는 시간을 더해줘야 함