# 모든 명함을 넣을 수 있는 지갑의 최소 크기(넓이)를 구해야 함
# 명함은 돌려서 넣을 수 있음(가로 세로 바뀌어도 됨)

def solution(sizes):
    w = []
    h = []
    for s in sizes:
        w.append(max(s))
        h.append(min(s))
    return max(w) * max(h)