# Trie 알고리즘

import sys
input = sys.stdin.readline

## Hash 풀이
t = int(input())
for _ in range(t):
    d = {}
    answer = "YES"
    n = int(input())
    for __ in range(n):
        d[input().strip()] = 1

    for num in d.keys():
        phone = ""
        for n in num:
            phone += n
            if phone in d and phone != num:
                answer = "NO"
    print(answer)

##  Trie 풀이

# class Node:
#     def __init__(self, key, data=None):
#         self.key = key
#         self.data = data
#         self.children = {}

# class Trie:
#     def __init__(self):
#         self.head = Node(None)
    
#     def insert(self, string):
#         curr = self.head

#         for c in string:
#             if c not in curr.children.keys():
#                 curr.children[c] = Node(c)
#             curr = curr.children[c]
#         curr.data = string
    
#     def starts_with_prefix_exist(self, prefix):
#         curr = self.head

#         for c in prefix:
#             if c in curr.children.keys():
#                 curr = curr.children[c]
#             else:
#                 return False
        
#         curr = [curr]
#         next = []
#         while True:
#             for node in curr:
#                 if node.data:
#                     return True
#                 next.extend(list(node.children.values()))
#             if len(next) != 0:
#                 curr = next
#                 next = []
#             else:
#                 break
#         return False

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     answer = "YES"
#     nums = []
#     for __ in range(n):
#         nums.append(input().strip())

#     nums.sort(key = lambda x:len(x), reverse=True)
#     trie = Trie()
#     for num in nums:
#         if trie.starts_with_prefix_exist(num):
#             answer = "NO"
#             break
#         trie.insert(num)

#     print(answer)