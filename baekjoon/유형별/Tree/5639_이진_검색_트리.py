import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

class Node:
    def __init__(self, number):
        self.number = number
        self.parent = -1
        self.left_child = -1
        self.right_child = -1

nodes = []
while True:
    try:
        k = int(input())
    except:
        break
    nodes.append(k)

def post_order(st, en):
    if st > en:
        return
    
    div = en + 1
    for j in range(st+1, en+1):
        if nodes[j] > nodes[st]:
            div = j
            break
    
    post_order(st+1, div-1) # 왼
    post_order(div, en) # 오
    print(nodes[st]) # 루

post_order(0, len(nodes) - 1)