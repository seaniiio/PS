# 3
# 2 2 2
# -> 2

N = int(input())
chains = list(map(int, input().split()))

chains.sort()
total_chains = len(chains)

ans = 0
while ans < total_chains - 1:
    chains[0] -= 1
    if chains[0] == 0:
        chains.remove(0)
        total_chains -= 1
    ans += 1

print(ans)