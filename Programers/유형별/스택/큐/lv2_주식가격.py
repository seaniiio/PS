def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        period = 1
        for j in range(i+1, len(prices) - 1):
            if prices[i] > prices[j]: break # 내 뒤에 나보다 낮은 가격이 있으면 break
            period += 1
        answer.append(period)
    answer.append(0) # 마지막 price의 지속시간은 무조건 0
    return answer