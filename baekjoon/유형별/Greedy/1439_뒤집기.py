# 1 -> 0으로 바뀌는, 0 -> 1로 바뀌는 횟수가 중요
# ex) 0001100은 0->1->0이므로 1번만 뒤집으면 됨
# 1 -> 0 -> 1, 1 -> 0 모두 1번만 뒤집으면 됨. 따라서 뒤집힌 횟수 // 2가 답

s = list(input())
latest_a = s[0]
cnt = 0
for a in s:
    if a != latest_a:
        cnt += 1
        latest_a = a

print((cnt+1) // 2)