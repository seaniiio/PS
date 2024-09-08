n = int(input())
tree = {}
for _ in range(n):
    v, left, right = input().split()
    tree[v] = [left, right]

def preorder(tree, node):
    if node == '.':
        return ''
    
    out = node
    out += preorder(tree, tree[node][0])
    out += preorder(tree, tree[node][1])

    return out

def inorder(tree, node):
    if node == '.':
        return ''

    out = ''
    out += inorder(tree, tree[node][0])
    out += node
    out += inorder(tree, tree[node][1])
    
    return out

def postorder(tree, node):
    if node == '.':
        return ''
    
    if len(tree[node]) == 0:
        return node
    
    out = ''
    out += postorder(tree, tree[node][0])
    out += postorder(tree, tree[node][1])
    out += node
    
    return out

print(preorder(tree, 'A'))
print(inorder(tree, 'A'))
print(postorder(tree, 'A'))