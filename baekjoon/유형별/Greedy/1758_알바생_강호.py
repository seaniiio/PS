import sys
input = sys.stdin.readline

n = int(input())
tips = []
for _ in range(n):
    tips.append(int(input()))
tips.sort(reverse=True)

total_tips = 0
for i, t in enumerate(tips):
    now_tip = t - i if t - i > 0 else 0
    total_tips += now_tip

print(total_tips)