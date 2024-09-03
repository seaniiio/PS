n = int(input())
dict = {}
for _ in range(n):
    k = int(input())
    if k not in dict.keys():
        dict[k] = 1
    else:
        dict[k] += 1

counter = []
for a, b in dict.items():
    counter.append((a, b))

counter.sort(key = lambda x:(x[1], -x[0]), reverse=True)
print(counter[0][0])