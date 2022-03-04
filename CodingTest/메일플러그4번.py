from collections import deque


def solution(board, c):
    table = [[9999 for _ in range(len(board[0]))] for _ in range(len(board))]  # 크기 9999의 board 초기화
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 2:
                start = [i, j]  # start 좌표저장
            if board[i][j] == 3:
                end = [i, j]  # end 좌표저장
    table[start[0]][start[1]] = 0  # 출발지를 0으로 초기화

    answer = (bfs(start, end, table, board, c))
    return answer


def bfs(start, end, table, board, c):  # 출발지, 도착지, table(9999로 초기화한 지도), board(기존 지도), c(자원에 들어가는 비용) 매개변수
    dx = [-1, 1, 0, 0]  #
    dy = [0, 0, -1, 1]  # 상하좌우를 담아줌
    x = start[0]
    y = start[1]  # x,y  좌표 담아줌

    n = len(board)  # 전체 지도 크기  y =  높이가  6
    m = len(board[0])  # x = 너비 10

    q = deque()  # 자료 형태 좌우로 뽑아지고, 좌우로 넣을 형태
    q.append((x, y))  # 튜플형태로 x, y를 집어넣음
    print(x, y)
    while q:  # q는 deque 자료구조인데 그 자료구조에 자료가 없을 때까지
        x, y = q.popleft()  # x, y를 뽑아냄
        for i in range(4):  # 4방향으로 계산
            nx = x + dx[i]  # 0일 때 왼쪽으로, 1일 때 오른쪽, 2일 때 아래로 한 칸, 3일 때 위로 한 칸
            ny = y + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0:  # 좌표 범위를 넘어가면 무시때림
                continue
            if board[nx][ny] == 0 or board[nx][ny] == 3:  # 열린길로 가거나 도착지로 갈 때
                if table[nx][ny] > table[x][y] + 1:  # nx, ny (다음좌표에 있는 값이 지금 좌표+1 보다 클 때)
                    table[nx][ny] = table[x][y] + 1  # 다음좌표는 지금좌표+1 한 값이 됨
                    q.append((nx, ny))  # 다음 좌표를 q 집어넣음
            elif board[nx][ny] == 1:  # 장애물이 있을 경우
                if table[nx][ny] > table[x][y] + 1 + c:  # nx, ny (다음좌표에 있는 값이 지금 좌표+1 +장애물 부순 크기 보다 클 때)
                    table[nx][ny] = table[x][y] + 1 + c  # 다음좌표는 지금좌표+1+c 한 값이 됨
                    q.append((nx, ny))
    for k in range(len(board)):
        print(table[k])  # 모든 최소의 값으로 이동하는 경우의 수 저장된 table

    return table[end[0]][end[1]]  # end 좌표를 table에서 찾은 값


board = [[0, 0, 0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 0, 1, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 3, 0, 0, 0, 1, 0]]
# 보드
c = 1
# 자원을 부수는 데 드는 비용
solution(board, c)