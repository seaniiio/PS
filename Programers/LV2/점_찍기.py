
def get_max(k, d):
    return (d // k) * k

def get_x(y, k, d):
    x = int(((d**2 - y**2) ** 0.5) // k)
    return x

def solution(k, d):
    answer = 0
    for i in range(d//k + 1):
        answer += (get_x(i*k, k, d) + 1)
    return answer