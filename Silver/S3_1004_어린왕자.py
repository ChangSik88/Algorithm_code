import math
from collections import deque
t=input()
anw=deque()

if t:
    t=int(t)
    for i in range(t):
        cnt=0
        x1,y1,x2,y2=map(int,input().split())
        n=int(input()) #행성의 개수. 
        x=(x1+x2)/2
        y=(y1+y2)/2
        r=math.sqrt((x1-x2)**2+(y1-y2)**2)/2

        for j in range(n):
            cx,cy,cr=map(int,input().split())
            distance=math.sqrt((cx-x)**2+(cy-y)**2)
            if distance+cr>r: 
                #중점거리+테스트원 반지름>메인원 반지름
                #출발-종료점의 거리를 지름으로 하는 원과 두 점에서 마주하는 원을 찾는 조건
                distStart=math.sqrt((x1-cx)**2+(y1-cy)**2)
                distEnd=math.sqrt((x2-cx)**2+(y2-cy)**2)
                if (distStart>cr and distEnd<cr) or (distStart<cr and distEnd>cr):
                    #시작/종료 두 점이 한 원 안에 있거나, 둘중 하나도 안에 있지 않아 지날 필요가 없는걸 거르는 조건
                    #위에서는 두 점에서 만나면 모두 가져왔기에 한번 더 체크를 해줘야했음
                    cnt+=1
        anw.append(cnt)

    for i in range(t):
        print(anw.popleft())
