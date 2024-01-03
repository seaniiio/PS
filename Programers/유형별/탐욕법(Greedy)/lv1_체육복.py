# 체육복을 도난당한 학생의 리스트와, 여분의 체육복을 가져온 학생의 리스트가 주어진다.
# 여분의 체육복을 가져온 학생들이 체육복을 도난당한 학생들에게 체육복을 빌려줘서, 최대한 많은 학생이 수업을 들을 수 있게 해야한다.
# 여분의 체육복을 가져왔으나 도난당했으면 다른사람에게 빌려줄 수 없다.

    
def solution(n, lost, reserve):
    lost_and_reserve = set(reserve) & set(lost) # 체육복을 가져온 학생이 도난당했으면 제외
    reserve = list(set(reserve) - lost_and_reserve)
    lost = list(set(lost) - lost_and_reserve)
    answer = n - len(lost)
    
    for lost_student in lost:
        if lost_student - 1 in reserve:
            answer += 1
            reserve.remove(lost_student - 1)
        elif lost_student + 1 in reserve:
            answer += 1
            reserve.remove(lost_student + 1)
            
    return answer