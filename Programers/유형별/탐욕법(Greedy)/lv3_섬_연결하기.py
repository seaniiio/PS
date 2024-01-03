# 섬 사이 다리를 짓는 데 소요하는 비용과, 섬의 개수가 주어진다
# [섬1, 섬2, 비용] -> 섬1과 섬2 사이의 다리 비용
# 모든 섬을 연결짓기 위한 최소 비용?

def solution(n, costs):
    answer = 0
    visited = []
    costs.sort(key=lambda x:x[2])
    visited.extend([costs[0][0], costs[0][1]])
    answer += costs[0][2]
    while len(visited) != n:
        for bridge in costs:
            if bridge[0] in visited and bridge[1] not in visited:
                visited.append(bridge[1])
                answer += bridge[2]
                break
            elif bridge[1] in visited and bridge[0] not in visited:
                visited.append(bridge[0])
                answer += bridge[2]
                break
    return answer