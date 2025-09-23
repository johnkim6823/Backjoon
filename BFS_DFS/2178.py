# 문제
# N * M 크기의 배열로 표현되는 미로

# 1 0 1 1 1 1
# 1 0 1 0 1 0
# 1 0 1 0 1 1  [ 예시 ]
# 1 1 1 0 1 1

# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다
# 이러한 미로가 주어졌을 때, (1,1)에서 출발하여 (N,M)의 위취로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
# 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력:
# 첫 째 줄에 두 정 수 N, M(2 <= N,M <= 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

from collections import deque

def bfs(maze, n, m):
    # 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 시작점 (0,0), 도착점 (n-1, m-1)
    queue = deque([(0, 0)])
    
    # 거리 배열 (방문체크 + 거리 기록)
    dist = [[0] * m for _ in range(n)]
    dist[0][0] = 1  # 시작점도 카운트
    
    while queue:
        x, y = queue.popleft()
        
        # 도착점 도달
        if x == n-1 and y == m-1:
            return dist[x][y]
        
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 체크
            if 0 <= nx < n and 0 <= ny < m:
                # 이동 가능하고 방문하지 않은 곳
                if maze[nx][ny] == 1 and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    
    return -1  # 도달 불가능

# 입력 처리
n, m = map(int, input().split())
maze = []

for _ in range(n):
    # 붙어있는 입력 처리
    row = list(map(int, list(input().strip())))
    maze.append(row)

# 최단 거리 출력
print(bfs(maze, n, m))