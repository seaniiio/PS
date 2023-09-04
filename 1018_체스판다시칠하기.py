import sys

x, y = map(int, sys.stdin.readline().split())
arr = ['null' for i in range(x)]

for i in range(x):
    arr[i] = input()

min = 32

for i in range(0, x-7):
    for j in range(0, y-7):
        draw1 = 0
        draw2 = 0
        for _i in range(8):
            for _j in range(8):
                if (_i+_j)%2 == 0 and arr[i+_i][j+_j] == 'B':
                    draw1 += 1
                elif (_i+_j)%2 == 0 and arr[i+_i][j+_j] == 'W':
                    draw2 += 1
                if (_i+_j)%2 == 1 and arr[i+_i][j+_j] == 'W':
                    draw1 += 1
                elif (_i+_j)%2 == 1 and arr[i+_i][j+_j] == 'B': 
                    draw2 += 1
        if(draw1 < min) : min = draw1
        if(draw2 < min) : min = draw2

print(min)
        