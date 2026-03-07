from collections import deque

anw=deque()
t=input()
if t:
    t=int(t)
    for p in range(t):
        x,y=map(int,input().split())
        distance=y-x
        half=distance/2
        sum,i=0,0
        while sum<half:
            i+=1
            sum+=i
        if i**2<distance:
            anw.append(i*2)
        elif i**2>=distance:
            anw.append(i*2-1)
    while anw:
        print(anw.popleft())