import sys
input = sys.stdin.readline

N = int(input())
keys = {}
for _ in range(N):
    find = False
    words = list(map(list, input().split()))

    for i, word in enumerate(words):
        if word[0].upper() not in keys: # 1번
            keys[word[0].upper()] = 0
            words[i].insert(0, "[")
            words[i].insert(2, "]")
            find = True
            break
    
    if not find:
        for i, word in enumerate(words):
            for j in range(1, len(word)):
                if not find and word[j].upper() not in keys: # 2번
                    keys[word[j].upper()] = 0
                    words[i].insert(j, "[")
                    words[i].insert(j+2, "]")
                    find = True
                    break

    for i, word in enumerate(words):
        words[i] = ''.join(word)

    print(' '.join(words))