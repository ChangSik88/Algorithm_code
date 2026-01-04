import sys
from collections import deque
T=sys.stdin.readline()
if T:
    T=int(T)
    anw=deque()
    for i in range(T):
        a,b=map(int,sys.stdin.readline().split())
        alist=[]
        alist.append(a%10)
        a_rest=a%10
        if a_rest==0:
            anw.append(10)
        else:
            a*=a
            while (a%10)!=a_rest:
                alist.append(a%10)
                a*=a_rest
            b_rest=b%len(alist)
            if b_rest==0:
                anw.append(alist.pop())
            else:
                anw.append(alist[b_rest-1])
    for i in range(T):
        print(anw.popleft())
