# A E I O U를 이용하여 만든 길이 5 이하의 단어들로 이루어진 사전이 있음
# 하나의 단어가 주어지면, 사전에 몇번째로 수록되어있는지 return해주기

from itertools import permutations

def solution(word):
    answer = 0
    alpha = "AAAAAEEEEEIIIIIOOOOOUUUUU"
    word_dictionary = []
    for i in range(1, 6):
        word_dictionary.extend(permutations(alpha, i))
    word_dictionary = [''.join(w) for w in word_dictionary]
    word_dictionary = sorted(list(set(word_dictionary)))
    
    return word_dictionary.index(word) + 1