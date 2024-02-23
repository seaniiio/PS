# 제한사항 보고 힙으로 풀어야 겠다고 생각함
# 테스트 케이스 하나만 틀렸었는데 -> end_flag 설정해주니 됐음

import heapq

end_flag = False

def work(h):
    global end_flag
    k = heapq.heappop(h)[1]
    if k == 0:
        end_flag = True
        return
    k -= 1
    heapq.heappush(h, [-k, k])
    
def sum_f(h):
    s = 0
    for a, b in h:
        s += (b ** 2)
    return s

def solution(n, works):
    answer = 0
    h = []
    for w in works:
        h.append([-w, w])
    heapq.heapify(h)
    while n != 0:
        n -= 1
        work(h)
        if end_flag:
            break
    return sum_f(h)