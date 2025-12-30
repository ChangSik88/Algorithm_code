from collections import deque
import math

def calculation(x,y,r1,r2):
    distance=math.sqrt(x**2+y**2)
    rMax=max(r1,r2)
    rMin=min(r1,r2)
    if distance>r1+r2 or distance+rMin<rMax: #안만날때
        return 0
    elif distance==r1+r2 or distance+rMin==rMax: #한 점에서 만날때
        return 1
    else: #두 점에서 만날때
        return 2

t=input()
if t:
    t=int(t)
    anw=deque()
    for i in range(t):
        x1,y1,r1,x2,y2,r2=map(int,input().split())
        if x1==x2 and y1==y2 and r1==r2: #답이 무한대일때
            anw.append(-1)
        else:
            x=x1-x2
            y=y1-y2
            tem=calculation(x,y,r1,r2)
            anw.append(tem)
    for i in range(t):
        print(anw.popleft())

