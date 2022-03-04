"""
NXN 크기의 2차원 배열 격자형태, 물건이 놓인 칸은 -1, 쌓여있는 먼지의 양은 0 이상의 정수
로봇청소기로 쌓여있는 먼지 청소,
go 현재 바라보는 방향 한칸 전진
left 왼쪽으로 회전
right 오른쪽으로 회전
로봇청소기가 방문한 칸은 먼지의 양이 0이 됨
현재 사무실의 상태를 나타내는 2차원 배열 office
로봇청소기가 놓여있는 칸의 좌표 r, c,
로봇청소기가 처리하는 명령어가 들어있는 배열 move
로봇청소기가 주어진 명령어를 모두 처리 후 청소한 먼지의 양을 return하는 함수 완성
단 로봇청소기는 처음에 항상 북쪽을 바라본 상태로 시작한다고 가정

-1은 물건이 놓여있어 지나갈 수 없는 칸
r은 북-남 방향의 좌표
c는 서-동 방향의 좌표
로봇청소기는 처음에 항상 0이상의 정수가 적혀있는 칸에만 놓여있음
move 배열에는 go, left, right단어만 들어있음


office			                r	c	move					                          result
[[5,-1,4], [6,3,-1],[2,-1,1]]	1	0	["go","go","right","go","right","go","left","go"] 	14

5  -1  4
6  3  -1
2  -1  1

"""

from collections import deque

def solution(office, r, c,move):
    global table
    global r2
    global c2
    table = [[0 for _ in range(len(office[0]))] for _  in range(len(office))]  #크기 9999의 board 초기화
    direction = 4
    dx = [-1, 1, 0, 0]  #
    dy = [0, 0, -1, 1]  # 상하좌우를 담아줌
    table[r][c] += office[r][c]
    office[r][c] = 0
    x = c
    y = r  # x,y  좌표 담아줌
    n = len(office)  # 전체 지도 크기  y =  높이가  6
    m = len(office[0])  # x = 너비 10
    for i in range(len(move)):
        print(i,move[i])
        print(office)
        print(table)
        if direction == 1 and move[i] == "left":
            direction =4
        elif direction == 1 and move[i] == "right":
            direction =3
        elif direction == 2 and move[i] == "left":
            direction =3
        elif direction == 2 and move[i] == "right":
            direction =4
        elif direction == 3 and move[i] == "left":
            direction =1
        elif direction == 3 and move[i] == "right":
            direction =2
        elif direction == 4 and move[i] == "left":
            direction =2
        elif direction == 4 and move[i] == "right":
            direction =1
        elif move[i] == "go":
            if direction == 1:
                nx = x + dx[1]  # 0일 때 왼쪽으로, 1일 때 오른쪽, 2일 때 아래로 한 칸, 3일 때 위로 한 칸
                ny = y + dy[1]
                if nx >= n or ny >= m or nx < 0 or ny < 0:  # 좌표 범위를 넘어가면 무시때림
                    continue
                if office[nx][ny] == -1:  # -1로 갈 때 막힘
                    continue
                else:  # 장애물이 있을 경우
                    table[nx][ny] = table[x][y] + office[nx][ny]  # 다음좌표는 지금좌표+1+c 한 값이 됨
                    r2 = ny
                    c2 = nx
                    office[nx][ny] = 0
            elif direction == 2:
                nx = x + dx[0]  # 0일 때 왼쪽으로, 1일 때 오른쪽, 2일 때 아래로 한 칸, 3일 때 위로 한 칸
                ny = y + dy[0]
                if nx >= n or ny >= m or nx < 0 or ny < 0:  # 좌표 범위를 넘어가면 무시때림
                    continue
                if office[nx][ny] == -1:  # -1로 갈 때 막힘
                    continue
                else:  # 장애물이 있을 경우
                    table[nx][ny] = table[x][y] + office[nx][ny]  # 다음좌표는 지금좌표+1+c 한 값이 됨
                    office[nx][ny] = 0
                    r2 = ny
                    c2 = nx
            elif direction == 3:
                nx = x + dx[2]  # 0일 때 왼쪽으로, 1일 때 오른쪽, 2일 때 아래로 한 칸, 3일 때 위로 한 칸
                ny = y + dy[2]
                if nx >= n or ny >= m or nx < 0 or ny < 0:  # 좌표 범위를 넘어가면 무시때림
                    continue
                if office[nx][ny] == -1:  # -1로 갈 때 막힘
                    continue
                else:  # 장애물이 있을 경우
                    table[nx][ny] = table[x][y] + office[nx][ny]  # 다음좌표는 지금좌표+1+c 한 값이 됨
                    office[nx][ny] = 0
                    r2 = ny
                    c2 = nx
            elif direction == 4:
                nx = x + dx[3]  # 0일 때 왼쪽으로, 1일 때 오른쪽, 2일 때 아래로 한 칸, 3일 때 위로 한 칸
                ny = y + dy[3]
                if nx >= n or ny >= m or nx < 0 or ny < 0:  # 좌표 범위를 넘어가면 무시때림
                    return
                if office[nx][ny] == -1:  # -1로 갈 때 막힘
                    return
                else:  # 장애물이 있을 경우
                    table[nx][ny] = table[x][y] + office[nx][ny]  # 다음좌표는 지금좌표+1+c 한 값이 됨
                    r2 = ny
                    c2 = nx
                    office[nx][ny] = 0
    return 0