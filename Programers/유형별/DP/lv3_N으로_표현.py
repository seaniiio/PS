# 표현해야 할 숫자 number, 사용할 수 있는 숫자 N이 주어진다.
# N의 사칙연산으로 number를 표현해야 할 때, N의 개수의 최솟값은?
# 최솟값이 8보다 크면 -1을 return한다.

def solution(N, number):
    answer = -1
    dp = [0]
    for i in range(1,9):
        this_set = set()
        this_set.add(int(str(N) * i))
        for cnt in range(1, i):
            for a in dp[cnt]:
                for b in dp[i-cnt]:
                    this_set.add(a + b)
                    this_set.add(a - b)
                    this_set.add(a * b)
                    if(b != 0):
                        this_set.add(a // b)
        dp.append(this_set)
        if number in this_set:
            answer = i
            break
    return answer
