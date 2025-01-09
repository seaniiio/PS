# 왼쪽 중 가장 높은 벽과 오른쪽 중 가장 높은 벽 찾기 -> 이게 고이는 기준

H, W = map(int, input().split())
walls = list(map(int, input().split()))

ans = 0
for i, wall in enumerate(walls):
    if (i == 0) or (i == len(walls) - 1):
        continue
    left_max = max(walls[:i]) # 왼쪽의 최댓값
    right_max = max(walls[i+1:]) # 오른쪽의 최댓값

    min_wall = min(left_max, right_max)
    if wall < min_wall:
        ans += (min_wall - wall)

print(ans)