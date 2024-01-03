# 해시 사용하지 않은 풀이
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            return answer   
    return answer

# 해시 사용한 풀이
def solution(phone_book):
    answer = True
    h = {}
    for p in phone_book:
        h[p] = 1
    for p in phone_book:
        prefix = ""
        for c in p:
            prefix = prefix + c
            if prefix != p and prefix in h:
                answer = False
                return answer
    return answer