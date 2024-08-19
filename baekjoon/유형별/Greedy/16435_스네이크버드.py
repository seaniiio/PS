n, L = map(int, input().split())
h_list = list(map(int, input().split()))
h_list.sort()

for h in h_list:
    if L >= h:
        L += 1

print(L)