n = int(input())
m = int(input())
s = input()

Pn = 'IO' * n + 'I'
N = 2 * n + 1

l = []
temp = 0
f = 'I'
for k in s:
    if temp == 0 and k == 'I':
        temp += 1
        f = 'O'
    elif k == 'O' and f == 'O':
        temp += 1
        f = 'I'
    elif k == 'I' and f == 'I':
        temp += 1
        f = 'O'
    elif k == 'I' and f == 'O':
        l.append(temp)
        f = 'O'
        temp = 1
    else:
        l.append(temp)
        temp = 0
if temp >= 3:
    l.append(temp)
    
sum = 0
for i in l:
    if i == N:
        sum += 1
    elif i > N:
        sum += (i - N) // 2 + 1
print(sum)

# 10101
# 1로시작하는 IOI 2개 ( 5 // 3 ) + 1
# IOIOI 1개 (5 // 5)
# IOIOIOI IOI 3개 (7 // 3) + 1
# IOIOIOI IOIOI 2개 (7 // 5) + 1