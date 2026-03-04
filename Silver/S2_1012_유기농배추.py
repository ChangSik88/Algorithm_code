from collections import deque
import sys
sys.setrecursionlimit(3000) 
#파이썬의 재귀 깊이제한은 1000으로 걸려있어서 recursion error가 발생
#따라서 제한을 늘려 문제 해결
#BFS로도 해당 문제 해결 가능할듯
def dfs(grid,x,y,m,n): #DFS 탐색 알고리즘으로 배추가 붙어있는 영역 확인
    if x<0 or x>=m or y<0 or y>=n or grid[y][x]==0:
        return False
    grid[y][x]=0 #1에 도달 시 0으로 바꿈
    dfs(grid,x-1,y,m,n) #좌
    dfs(grid,x+1,y,m,n) #우
    dfs(grid,x,y+1,m,n) #상
    dfs(grid,x,y-1,m,n) #하
    return True #탐색 완료(시작 지점이 1일때) True 반환

def bfs(grid,x,y,m,n): #BFS로 해결(재귀 에러 처리 위함)
    if grid[y][x]==0: #0인건 빠르게 걸러냄
        return False
    que=deque([(x,y)]) #첫 좌표 기준 큐 생성
    while que: #큐에 좌표가 있을 때
        nx,ny=que.popleft()
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        for i in range(4): #상하좌우 탐색
            kx=nx+dx[i]
            ky=ny+dy[i]
            if kx>=0 and kx<m and ky>=0 and ky<n: #범위 이탈 체크
                if grid[ky][kx]==1: #배추가 심겼는지 체크
                    grid[ky][kx]=0 #방문 표시
                    que.append((kx,ky)) #방문 장소 큐에 추가 후 반복
    return True    
    


t=input()
if t:
    t=int(t)
    anw=deque()
    for i in range(t):
        cnt=0
        m,n,k = map(int,input().split())
        grid=[[0]*m for _ in range(n)]
        for j in range(k):
            x,y=map(int,input().split())
            grid[y][x]=1
        for i in range(0,n):
            for j in range(0,m):
                if bfs(grid,j,i,m,n)==True: #반환값이 True면
                    cnt+=1 #카운트 +1
        anw.append(cnt)
    for i in range(t):
        print(anw.popleft())
    

