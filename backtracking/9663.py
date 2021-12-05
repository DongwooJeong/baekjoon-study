import sys 
n = int(sys.stdin.readline()) 
board = [0] * n 
ans_count = 0 
visited = [False] * n # n번째 열에 퀸이 있는지를 표시하는 list 

def check(x): # 기존에 있는 퀸들과 대각선 방향으로 겹치는 퀸이 있는지를 확인 
    for i in range(x): 
        if abs(board[x] - board[i]) == x - i: 
            return False 
    return True 
def n_queen(x): 
    global ans_count 
    if x == n: 
        ans_count += 1 
        return 
    for i in range(n): 
        if visited[i]: # i번째 열에 퀸이 있을 경우 continue 
            continue 
        
        board[x] = i 
        if check(x): 
            visited[i] = True 
            n_queen(x + 1) 
            visited[i] = False 
n_queen(0) 
print(ans_count)

