# 문제
# 우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다.
# 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다.
#  예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

# 입력
# 사람들은 1,2,3, ... n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다.
# 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다.
# 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다.
# 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.
# 각 사람의 부모는 최대 1명만 주어진다. 
# 관계 없을 시 -1 출력

from collections import deque

def bfs(start, end):
    queue = deque([start])
    distance = [-1] * (n + 1)
    distance[start] = 0
    
    while queue:
        node = queue.popleft()
        
        if node == end:
            return distance[end]
        
        for next_node in graph[node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[node] + 1
                queue.append(next_node)
    
    return -1

# 입력
n = int(input())
a, b = map(int, input().split())
m = int(input())

# 그래프 생성
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 출력
print(bfs(a, b))