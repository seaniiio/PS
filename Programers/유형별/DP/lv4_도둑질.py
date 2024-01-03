# 각 집마다 가지 돈에 대한 리스트가 주어진다.
# 집은 동그랗게 배치되어있다.
# 인접한 집은 털 수 없을 때, 각 집을 털어 얻을 수 있는 돈의 최댓값은?

def solution(money):
    answer = 0
    dp_o = [0 for _ in range(1000000)] # 첫 번째 집을 터는 경우
    dp_x = [0 for _ in range(1000000)] # 첫 번째 집을 안터는 경우
    dp_o[0] = money[0]
    dp_o[1] = money[0]
    dp_x[1] = money[1]
    if len(money) == 3:
        dp_o[2] = money[0]
    else:
        dp_o[2] = money[0] + money[2]
    dp_x[2] = max(money[1], money[2])
    for i in range(3, len(money)):
        if i == len(money) - 1: # 마지막 집
            dp_o[i] = dp_o[i-1]
            dp_x[i] = max(dp_x[i-2] + money[i], dp_x[i-1])
            break
        dp_o[i] = max(dp_o[i-1], dp_o[i-2] + money[i])
        dp_x[i] = max(dp_x[i-1], dp_x[i-2] + money[i])
        # 점화식이 왜 이렇게?
        # 이전 집을 털었을 때, 현재 집은 털지 못함. 이 경우는 dp[i-1]
        # 전전 집을 털고 이전 집을 털지 않았을 때, 현재 집을 털 수 있음. 이 경우는 dp[i-2] + money[i]
    return max(dp_o[len(money) - 1], dp_x[len(money) - 1])


# 동그랗게 둘러사여 있기 때문에, 첫 번째 집을 털면 마지막 집을 털 수 없다
# 따라서 두개의 dp list(첫 번째 집 털었을 때, 안털었을 때)를 만들어 관리해준다