# 무인도에 갇힌 사람들의 몸무게 list가 주어진다
# 구명보트로 이들을 구조해야 하는데, 한계 무게가 존재하고, 최대 2명까지 탈 수 있다
# 사람들을 다 옮기기 위해 필요한 최소한의 구명보트의 수는?

from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            answer += 1
            people.pop()
            people.popleft()
        else:
            people.pop()
            answer += 1
    answer += len(people)
    return answer