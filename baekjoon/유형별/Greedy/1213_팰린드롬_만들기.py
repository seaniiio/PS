# string에서 각 알파벳이 몇 번 나왔는지 확인 -> Counter 사용
# string 뒤집을땐 [::-1]

from collections import Counter

alpha = Counter(list(input()))
answer = ""
possible = True

cnt = 0
for k, v in alpha.items():
    if v % 2 == 1:
        cnt += 1
        if cnt == 2:
            possible = False
            break

center = ""
if possible:
    for k, v in sorted(alpha.items()):
        if v % 2 == 1:
            center = k
        answer += k * (v // 2)
    answer += (center +  answer[::-1])
else:
    answer = "I'm Sorry Hansoo"

print(answer)
