global answer, find
answer = 50
find = False

def ok(a, b): # 두 단어가 하나 제외 겹치면
    cnt = 0
    for i, j in zip(a, b):
        if i == j: cnt += 1
    if cnt == len(a) - 1:
        return True
    return False

def DFS(w, cnt, target, words):
    global answer, find
    if w == target:
        answer = min(answer, cnt)
        find = True
        return
    for word in words:
        if ok(w, word) and visited[word] == False:
            visited[word] = True
            DFS(word, cnt+1, target, words)
            visited[word] = False

def solution(begin, target, words):
    global visited, find, answer
    visited = {t : False for t in words}
    visited[begin] = True
    DFS(begin, 0, target, words)
    if find == True:
        return answer
    else:
        return 0
    
    