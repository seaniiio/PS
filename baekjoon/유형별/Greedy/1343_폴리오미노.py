# X가 4개 -> A로
# X가 2개 -> B로
# 

s = list(input())
ans = s[:]
no_ans = False
cnt = 0
for i, c in enumerate(s):
    if c == 'X':
        cnt += 1
        if cnt == 4:
            for j in range(i-3, i+1):
                ans[j] = 'A'
            cnt = 0
        if i == len(s) - 1 and cnt == 2:
            ans[i], ans[i-1] = 'B', 'B'
            cnt = 0
    elif c == '.':
        if cnt == 2:
            for j in range(i-2, i):
                ans[j] = 'B'
            cnt = 0
        elif cnt == 0:
            ans[i] = '.'
        else:
            no_ans = True
            break
    if i == len(s)-1:
        if cnt != 0:
            no_ans = True

if not no_ans:
    print(''.join(ans))
else:
    print(-1)