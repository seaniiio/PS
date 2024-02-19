str = input()
n = len(str)
s = []
answer = 0
result = 1

for i in range(n):
    if str[i] == '(':
        s.append(str[i])
        result *= 2
    elif str[i] == '[':
        s.append(str[i])
        result *= 3
    elif str[i] == ')':
        if len(s) == 0 or s[-1] != '(':
            answer = 0
            break
        elif s[-1] == '(' and str[i-1] == '(': 
            answer += result
        result //= 2
        s.pop()
    elif str[i] == ']':
        if len(s) == 0 or s[-1] != '[':
            answer = 0
            break
        elif s[-1] == '[' and str[i-1] == '[': 
            answer += result
        result //= 3
        s.pop()
if len(s) != 0:
    answer = 0
print(answer)