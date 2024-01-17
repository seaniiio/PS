x, y = map(int, input().split())
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT", ]

now = sum(month[:x]) + y
print(day[now % 7])
