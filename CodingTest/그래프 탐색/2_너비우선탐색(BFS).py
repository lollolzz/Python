"""
날짜 : 2021/10/08
이름 : 권능한
내용 : 코딩테스트 - 그래프 탐색 BFS 실습하기
"""

from collections import deque

# BFS 함수 정의
def bfs(graph, start_node):
    visited = []

    queue = deque([start_node])
    visited.append(start_node)

    while queue:
        current = queue.popleft()

        for x in graph[current]:  # 현재노드의 인접노드 탐색
           if x not in visited:   # 인접노드가 방문하지 않았으면
                queue.append(x)   # 인접노드 큐 저장
                visited.append(x) # 인접노드 방문처리

    return visited

# 그래프를 인접 리스트로 구현
graph = [[],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]]

# BFS 실행
result = bfs(graph, 1)
print(result)
