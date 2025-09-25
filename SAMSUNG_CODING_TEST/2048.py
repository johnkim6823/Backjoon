# 문제
# 2048 게임은 4x4 크기의 보드에서 혼자 즐기는 재밌는 게임이다. 
# 이 게임에서 한 번으 ㅣ이동은 보드 위에 있는 전체블록을 상하자우 네 방향 중 하나로 이동시키는 것이다.
# 이때, 같을 갖는 두 블록이 충돌하면 두 불록은 하나로 합쳐지게 된다.
# 한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.
# 마지막으로, 똑같은 수가 세개가 있는 경우에는 이동하려는 하는 쪽의 칸이 먼저 합쳐진다. 예를 들어, 이동시키는 경우에는 위쪽에 있는 불록이 먼저 합쳐지게된다.
# 이 문제에서는 N x N의 보드 크기를 가졍한다. 보드의 크기와 보드 판의 블록 상태가 주어졌을 때, 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다. 0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다. 블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다. 블록은 적어도 하나 주어진다.

# 보드의 크기 N
n = 0
# 최종 결과를 저장할 변수
max_block = 0

# 90도 시계 방향으로 회전하는 함수
def rotate(board):
    global n
    new_board = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            new_board[c][n - 1 - r] = board[r][c]
    return new_board

# 블록을 왼쪽으로 밀고 합치는 함수
def slide(board):
    global n
    new_board = []
    for row in board:
        # 1. 0이 아닌 블록만 추출
        blocks = [val for val in row if val != 0]
        
        # 2. 블록 합치기
        merged_row = []
        i = 0
        while i < len(blocks):
            # 다음 블록이 있고, 현재 블록과 값이 같다면 합친다
            if i + 1 < len(blocks) and blocks[i] == blocks[i+1]:
                merged_row.append(blocks[i] * 2)
                i += 2
            else:
                merged_row.append(blocks[i])
                i += 1
        
        # 3. 0 채워넣기
        new_row = merged_row + [0] * (n - len(merged_row))
        new_board.append(new_row)
        
    return new_board

# DFS 함수
def dfs(board, count):
    global n, max_block

    # 현재 보드에서 가장 큰 블록을 찾아 max_block 갱신
    for r in range(n):
        for c in range(n):
            if board[r][c] > max_block:
                max_block = board[r][c]

    # 5번 이동했으면 종료
    if count == 5:
        return

    # --- 4방향으로 이동하여 다음 상태 탐색 ---
    
    # 1. 위로 이동
    # 270도 회전 -> slide -> 90도 회전
    board_up = rotate(rotate(rotate(board)))
    board_up = slide(board_up)
    board_up = rotate(board_up)
    dfs(board_up, count + 1)
    
    # 2. 아래로 이동
    # 90도 회전 -> slide -> 270도 회전
    board_down = rotate(board)
    board_down = slide(board_down)
    board_down = rotate(rotate(rotate(board_down)))
    dfs(board_down, count + 1)

    # 3. 왼쪽으로 이동
    board_left = slide(board)
    dfs(board_left, count + 1)

    # 4. 오른쪽으로 이동
    # 180도 회전 -> slide -> 180도 회전
    board_right = rotate(rotate(board))
    board_right = slide(board_right)
    board_right = rotate(rotate(board_right))
    dfs(board_right, count + 1)


def main():
    global n, max_block
    n = int(input())
    
    initial_board = []
    for _ in range(n):
        row = list(map(int, input().split()))
        initial_board.append(row)
        
    max_block = 0
    dfs(initial_board, 0)
    print(max_block)

# 실행
main()