import sys

input = sys.stdin.readline

a, b = map(int, input().split())
m_a, m_b = [], []

for _ in range(a):
    m_a.append(list(input().strip()))
for _ in range(a):
    m_b.append(list(input().strip()))

cnt = 0

def reverse_m(i, j, m_a):
    if i < len(m_a) - 2 and j < len(m_a[0]) - 2:
        for _i in range(i, i+3):
            for _j in range(j, j+3):
                m_a[_i][_j] = '0' if m_a[_i][_j] == '1' else '1' 
    return m_a

for i in range(a):
    for j in range(b):
        if m_a[i][j] != m_b[i][j]:
            m_a = reverse_m(i, j, m_a)
            cnt += 1

for i in range(a):
    for j in range(b):
        if m_a[i][j] != m_b[i][j]:
            cnt = -1

print(cnt)