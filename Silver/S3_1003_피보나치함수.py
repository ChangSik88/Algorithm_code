from collections import deque

def fibonachi(n):
    a=[0]*(n+1)
    b=[0]*(n+1)
    a[0],b[0],a[1],b[1]=1,0,0,1
    for i in range(2,n+1):
        a[i]=a[i-1]+a[i-2]
        b[i]=b[i-1]+b[i-2]
    print(a[n],b[n])


T=input()
num=deque()
if T:
    T=int(T)
    for i in range(T):
        N=int(input())
        num.append(N)
    for i in range(T):
        N=num.popleft()
        if N>=1:
            fibonachi(N)
        else:
            print(1,0)

