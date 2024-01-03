# 모든 차가 고속도로에 들어오는 지점, 나간 지점이 주어진다.
# 모든 차를 감시하기 위해 필요한 최소한의 카메라 개수?

def solution(routes):
    answer = 1
    camera = []
    routes.sort(key=lambda x:x[0], reverse=True)
    camera.append(routes[0][0])
    for route in routes:
        if camera[-1] >= route[0] and camera[-1] <= route[1]:
            continue
        else:
            camera.append(route[0])
            answer += 1
    return answer