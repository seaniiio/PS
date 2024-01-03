# 리스트에서 값이 h이상인 원소가 h개 이상이면, answer = h
# h의 최댓값이 answer가 됨

def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True) # 우선 내림차순으로 sort
    n = len(citations)
    for i in range(1, n):
        if citations[i - 1] >= i and citations[i] <= i: # h번째 원소를 확인했을 때, h 이상이면 만족
            answer = i
    # 인덱싱에서 오류가 떠서, 값이 n 이상인 원소가 n개인 경우, 즉 모든 원소가 n 이상인 경우를 따로 뺌
    if citations[-1] >= n:
        answer = n
    return answer