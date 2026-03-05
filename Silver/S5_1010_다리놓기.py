import sys
from math import factorial
from collections import deque
t=sys.stdin.readline()
anw=deque()
if t:
    t=int(t)
    for i in range(t):
        n,m=map(int,sys.stdin.readline().split())
        tem=int((factorial(m))/(factorial(n)*factorial(m-n)))
        #조합식 n!/r!(n-r)!
        anw.append(tem)
    while anw:
        print(anw.popleft())
#푸시용 주석


