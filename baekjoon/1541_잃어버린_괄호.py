str = list(input().split('-'))

def plus(str):
    p = map(int, str.split('+'))
    return sum(p)

result = plus(str[0].rstrip())
for i in range(1, len(str)):
    result -= plus(str[i].rstrip())
print(result)