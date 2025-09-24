def dfs(node):
    visited[node] = True
    result.append(node)
    
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

# 입력
n, m, v = map(int, input().split())

# 그래프 생성
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in range(1, n + 1):
    graph[i].sort()

# DFS 실행
visited = [False] * (n + 1)
result = []
dfs(v)

# 출력
print(' '.join(map(str, result)))