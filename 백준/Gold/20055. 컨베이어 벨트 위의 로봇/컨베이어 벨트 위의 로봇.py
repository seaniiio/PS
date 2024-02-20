import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lim_l = list(map(int, input().split()))

lim = {i : lim_l[i] for i in range(n * 2)}
robot = {i : False for i in range(n * 2)}
#robot = [False for _ in range(n * 2)]
cur = 0
ans = 0
r = set([])

def cir(cur): # cur + (n-1)번째가 내리는 위치
    new_cur = cur - 1
    if cur == 0:
        new_cur = 2*n - 1
    return new_cur
    
def on(cur): # 로봇을 cur위치에 올림(내구도 있으면)
    global robot, lim
    if lim[cur] > 0:
        robot[cur] = True
        lim[cur] -= 1

def move(i): # i번째 위치의 로봇을 i+1번째에 옮길 수 있으면 옮김
    global robot, lim, r
    new_i = (i+1) % (2*n)
    if robot[i] == True and robot[new_i] == False and lim[new_i] > 0:
        lim[new_i] -= 1 # 내구도 1 감소
        if lim[new_i] == 0:
            r.add(new_i)
        robot[new_i], robot[i] = True, False # 로봇 옮김

def out(cur): # 내리는 위치의 로봇 내림
    global robot
    robot[((cur + (n-1)) % (2*n))] = False

def cnt(target): # 내구도가 0인게 k개이면 True
    c = 0
    for k in lim:
        if k == 0:
            c += 1
    if c >= target:
        return True
    return False

while True:
    ans += 1
    # 1단계: 한 칸 회전
    cur = cir(cur)
    out(cur)
    # 2단계: 로봇 옮기기
    for i in range(n-2, -1, -1):
        move((cur + i) % (2*n))
    out(cur)
    # 3단계: 로봇 올리기
    on(cur)
    if lim[cur] == 0:
        r.add(cur)
    if len(r) >= k:
        print(ans)
        break