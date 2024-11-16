# top이 *, -인데 현재 +, - -> 쭉 전부 pop
# 현재 ( -> )나오면 (나올때까지 pop

from collections import deque

str = input()
ans = ""
operator = deque([])
operator_type = ["+", "-", "*", "/", "(", ")"]

for c in str:
    if c not in operator_type:
        ans += c
        continue
    if c in ("+", "-"):
        while len(operator) != 0 and operator[-1] != "(":
            ans += operator.pop()
        operator.append(c)
    elif c in ("*", "/"):
        while len(operator) != 0 and (operator[-1] == "*" or operator[-1] == "/"):
            ans += operator.pop()
        operator.append(c)
    elif c == ")":
        while len(operator) != 0 and operator[-1] != "(":
            ans += operator.pop()
        operator.pop()
    else:
        operator.append(c)

while len(operator) != 0:
    ans += operator.pop()

print(ans)