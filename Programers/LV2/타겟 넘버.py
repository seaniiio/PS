# DFS/BFS 문제
# n개의 정수들의 순서를 바꾸지 않고 적절히 +, -를 해서 target number를 만드는 경우의 수 구하기

def solution(numbers, target):
    answer = DFS(0, numbers, target)
    return answer

def DFS(depth, numbers, target):
    answer = 0
    if depth < len(numbers) - 1:
        # 현재 숫자가 +인 경우
        answer += DFS(depth+1, numbers, target)
        # 현재 숫자가 -인 경우
        numbers[depth] *= (-1)
        answer += DFS(depth+1, numbers, target)
        
    if depth == len(numbers) - 1:
        if sum(numbers) == target:
            return 1
        numbers[depth] *= (-1)
        if sum(numbers) == target:
            return 1
    return answer

# 각 숫자에 대해 +인 경우, -인 경우를 모두 탐색해야 함 -> DFS 사용
# DFS의 경우 **depth**를 꼭 정의해줘야 한다는 것을 잊지 말자.
    