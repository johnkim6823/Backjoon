# 문제
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
# 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

def dfs(x, y):
    # 범위 체크
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    
    # 집이 없거나 이미 방문한 경우
    if graph[x][y] == 0:
        return 0
    
    # 방문 처리
    graph[x][y] = 0  # 방문한 집은 0으로 변경
    count = 1  # 현재 집 카운트
    
    # 상하좌우 탐색
    count += dfs(x-1, y)  # 상
    count += dfs(x+1, y)  # 하
    count += dfs(x, y-1)  # 좌
    count += dfs(x, y+1)  # 우
    
    return count

# 입력
n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, list(input().strip()))))

# 각 단지의 집 개수 저장
complexes = []

# 모든 위치 탐색
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            # 새로운 단지 발견
            size = dfs(i, j)
            complexes.append(size)

# 출력
print(len(complexes))  # 단지 수
complexes.sort()  # 오름차순 정렬
for size in complexes:
    print(size)