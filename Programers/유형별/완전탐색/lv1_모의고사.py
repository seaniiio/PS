# 3명의 수포자가 찍는 방식이 주어진다.
# 문제들에 대한 답이 주어진다.
# 모든 수포자중 가장 높은 점수를 갖는 수포자의 번호를 return한다.

def solution(answers):
    answer = []
    student1 = "12345" * 2000
    student2 = "21232425" * 1250
    student3 = "3311224455" * 1000
    score = [0, 0, 0]
    for i in range(len(answers)):
        if int(student1[i]) == answers[i]:
            score[0] = score[0] + 1
        if int(student2[i]) == answers[i]:
            score[1] = score[1] + 1
        if int(student3[i]) == answers[i]:
            score[2] = score[2] + 1
    maxN = max(score)
    for i in range(len(score)):
        if maxN == score[i]:
            answer.append(i + 1)
    return answer