"""
날짜 : 21/08/20
이름 : 권능한
내용 : 코딩 테스트 - 상하좌우

"""


#n값 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split() #문자열을 쪼개서 list로 만들어 준다

for plan in plans:
    if plan == 'L':
        if y == 1:
            continue # if 조건을 충족한다면 continue하겟다 그냥 무시하겟다
        else:
            y -= 1

    if plan == 'R':
        if y == n: # y가 행이기 때문에 y가 n이라면 n이상 + 할 수 없기 때문에 continue
            continue
        else:
            y += 1

    if plan == 'U': # 이하 밑 부분은 위의 내용을 참조해서 해석하면 된다. 동일
        if x == 1:
            continue
        else:
            x -= 1

    if plan == 'D':
        if x == n:
            continue
        else:
            x += 1

print(x, y)
"""
n = int(input())
x, y = 1, 1
plans = input().split()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나면 무시
    if nx < 1 or ny < 1 or nx > n or ny > n: #n의 범위에서 벗어나는 숫자가 있을 경우 continue
        continue
    # 이동하기
    x, y = nx, ny
print(x, y)
"""












#최종 좌표 출력
print(x,y)
