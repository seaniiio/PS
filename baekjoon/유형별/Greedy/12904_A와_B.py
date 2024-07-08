s = input()
t = input()

t_list = list(t)
rev = False

while len(s) != len(t_list):
    if rev == True:
        if t_list[0] == 'B':
            rev = False
        t_list = t_list[1:]
    else: # rev == False
        if t_list[-1] == 'B':
            rev = True
        t_list = t_list[:-1]

result = 1
if rev == False:
    for i in range(len(s)):
        if s[i] != t_list[i]:
            result = 0
else: # rev == True
    for i in range(len(s)):
        if s[i] != t_list[len(s)-i-1]:
            result = 0

print(result)