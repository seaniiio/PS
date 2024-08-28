n = int(input())
nums = {i:0 for i in range(1, n+1)}
for i in range(1, n+1):
    nums[i] = int(input())



def dfs(start):
    visited = [False for _ in range(n+1)]
    global set_nums
    visited_this = [start]
    visited[start] = True
    stk = [start]

    while len(stk) != 0:
        next = nums[stk.pop()]
        if next == start:
            set_nums.extend(visited_this)
            return
        if visited[next] == False:
            visited[next] = True
            visited_this.append(next)
            stk.append(next)

set_nums = []
for i in range(1, n+1):
    if i not in set_nums:
        dfs(i)

set_nums_set = list(set(set_nums))
print(len(set_nums_set))
set_nums_set.sort()
for k in set_nums_set:
    print(k)
