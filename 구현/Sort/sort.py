# 선택정렬
# 처리되지 않은 데이터 중 가장 작은 데이터를 선택에 맨 앞에 있는 데이터와 바꾸는 것을 반복
# O(n^2)

def selection_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i+1, len(l)):
            if l[min_index] > l[j]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    return l

l = [5, 1, 6, 2, 8, 7, 4, 3]
print(selection_sort(l))

# 삽입정렬
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
# O(n^2)

def insertion_sort(l):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j-1]: # 한 칸씩 이동
                l[j], l[j-1] = l[j-1], l[j]
            else:
                break
    return l

l = [5, 1, 6, 2, 8, 7, 4, 3]
print(insertion_sort(l))

# 퀵정렬
# 기준 데이터를 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
# avg: O(NlogN), worst: O(N^2)

def quick_sort(l):
    if len(l) <= 1:
        return l
    pivot = l[0]
    tail = l[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

l = [5, 1, 6, 2, 8, 7, 4, 3]
print(quick_sort(l))

# 계수정렬
# 특정한 조건이 부합할 때만 사용할 수 있지만, 매우 빠르게 동작하는 정렬 알고리즘
# O(N + K) 보장 (K: 데이터 중 최댓값)

def counting_sort(l):
    count = [0] * (max(l) + 1)
    result = []

    for num in l:
        count[num] += 1
    
    for i, c in enumerate(count):
        for _ in range(c):
            result.append(i)
    
    return result

l = [5, 1, 6, 2, 8, 7, 4, 3]
print(counting_sort(l))