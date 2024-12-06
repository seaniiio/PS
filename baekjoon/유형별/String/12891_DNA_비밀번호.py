S, P = map(int, input().split())
s = list(input())
a, c, g, t = map(int, input().split())


bef_dic = {"A" : 0, "C" : 0, "G" : 0, "T" : 0}
ans = 0
for j in range(P):
    bef_dic[s[j]] += 1
if bef_dic["A"] >= a and bef_dic["C"] >= c and bef_dic["G"] >= g and bef_dic["T"] >= t:
    ans += 1

for i in range(1, S-P+1):
    dic = bef_dic
    dic[s[i-1]] -= 1
    dic[s[i+P-1]] += 1

    if dic["A"] >= a and dic["C"] >= c and dic["G"] >= g and dic["T"] >= t:
        ans += 1
    
    bef_dic = dic

print(ans)
