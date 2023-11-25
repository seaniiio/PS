n = int(input())
count = 1
num = 666
while(n != count):
    num += 1
    if(str(num).find('666') != -1):
        count += 1

print(num)