n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
idx_A, idx_B = 0, -1

for _ in range(k):
    if A[idx_A] < B[idx_B]:
        A[idx_A], B[idx_B] = B[idx_B], A[idx_A]
        idx_A += 1
        idx_B -= 1
    else:
        break

print(sum(A))