# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력: 
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

from collections import deque

def dfs(graph, v, visited, result):
    visited[v] = True
    result.append(v)
    
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(graph, next_v, visited, result)

def bfs(graph, v, n):
    visited = [False] * (n + 1)
    result = []
    queue = deque([v])
    visited[v] = True
    
    while queue:
        cur = queue.popleft()
        result.append(cur)
        
        for next_v in graph[cur]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)
    
    return result

# 입력
n, m, v = map(int, input().split())

# 인접 리스트 초기화
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향

# 정렬 (작은 번호부터 방문)
for i in range(1, n + 1):
    graph[i].sort()

# DFS 수행
visited_dfs = [False] * (n + 1)
result_dfs = []
dfs(graph, v, visited_dfs, result_dfs)

# BFS 수행
result_bfs = bfs(graph, v, n)

# 출력
print(' '.join(map(str, result_dfs)))
print(' '.join(map(str, result_bfs)))