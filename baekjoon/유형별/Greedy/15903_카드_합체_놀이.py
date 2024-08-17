n, m = map(int, input().split())
cards =list(map(int, input().split()))

for _ in range(m):
    cards.sort()
    two_sum = cards[0] + cards[1]
    cards[0], cards[1] = two_sum, two_sum

print(sum(cards))