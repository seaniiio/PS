# N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.
# 단어 10개 입력 -> 
# 알파벳별로 가중치 구하기 -> weight

num = int(input())
word = []
for i in range(num):
    word.append(input())
weight = [10 ** i for i in range(0, 8)]
alpha = {} # 알파벳별로 가중치 저장 -> 할당된 값 저장

for w in word:
    l = len(w) - 1
    for idx, c in enumerate(w):
        if c in alpha.keys():
            alpha[c] += weight[l - idx]
        else:
            alpha[c] = weight[l - idx]

alpha_list = []
for a in alpha.keys():
    alpha_list.append([a, alpha[a]])

alpha_list.sort(key = lambda x : -x[1])
for i in range(len(alpha_list)):
    alpha[alpha_list[i][0]] = 9 - i

ans = 0

for w in word:
    l = len(w) - 1
    for idx, c in enumerate(w):
        ans += 10 ** (l - idx) * alpha[c]

print(ans)

