import sys
input = sys.stdin.readline

trees = {}
total = 0
while True:
    tree = input().rstrip()
    if tree:
        total += 1
        if tree in trees:
            trees[tree] += 1
        else:
            trees[tree] = 1
    else:
        break

trees_sorted = list(trees.keys())
trees_sorted.sort()

for k in trees_sorted:
    print("%s %.4f" % (k, trees[k]/total*100))