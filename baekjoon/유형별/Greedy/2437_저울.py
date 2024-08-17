# 추 하나씩 작은것부터 추가해가면서 잴 수 없는 무게 찾기
# k번째 추를 추가했을 때 연속적인 무게가 깨진다 -> 이전까지의 무게합 + 1이 만들수없는 최솟값

n = int(input())
weights = list(map(int, input().split()))
weights.sort()
available = 0

for w in weights:
    if available + 1 < w:
        break
    available += w
        
print(available + 1)