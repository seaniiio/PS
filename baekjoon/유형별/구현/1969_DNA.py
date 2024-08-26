n, m = map(int, input().split())
s_list = []

for _ in range(n):
    s_list.append(input())

answer = ''
cnt = 0
for i in range(m):
    dna = [0, 0, 0, 0] # A, C, G, T
    dna_d = {'A' : 0, 'C' : 1, 'G' : 2, 'T' : 3}
    dna_d_2 = {0 : 'A', 1 : 'C', 2 : 'G', 3 : 'T'}

    for s in s_list:
        dna[dna_d[s[i]]] += 1
    max_d = max(dna)
    for d_i, d in enumerate(dna):
        if d == max_d:
            answer += dna_d_2[d_i]
            cnt += n - max_d
            break

print(answer)
print(cnt)