# 키가 큰 사람부터 순서대로 배치

# n = int(input())
# left = list(map(int, input().split()))
# left = left[::-1]
# line = [len(left)]

# for i in range(1, len(left)): # 키 큰순서부터
#     # 0 <= left[i] <= i 
#     if left[i] == 0:
#         line = [len(left) - i] + line
#     elif left[i] == len(left) - 1:
#         line = line + [len(left) - i]
#     else:
#         line = line[:left[i]] + [len(left) - i] + line[left[i]:]

# for p in line:
#     print(p, end=' ')

# 작은 순서부터 채우는 방법
# 현재 "0"인 위치 -> 무조건 현재 나보다 큰 사람이 위치

n = int(input())
left = list(map(int, input().split()))
line = [0] * n

for i in range(n):
    cnt = 0
    idx = 0
    while idx < n:
        if cnt == left[i] and line[idx] == 0:
            line[idx] = i+1
            break
        elif line[idx] == 0:
            cnt += 1
        idx += 1

print(' '.join(map(str, line)))