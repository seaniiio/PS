import sys
input = sys.stdin.readline

n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)

max_weight = rope[0]

for i in range(1, len(rope)):
    if rope[i] * (i+1) > max_weight:
        max_weight = rope[i] * (i+1)

print(max_weight)