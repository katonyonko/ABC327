import io
import sys
import pdb
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
from bisect import bisect_right, bisect_left
from math import gcd
import math

_INPUT = """\
6
3
1000 600 1200
3
600 1000 1200
1
100
"""

# P=[1000, 600, 1200]
# tmp=[0, 1, 1.9, 2.71]
# j=2
# i=2
# print(((-200+1200/((j-1)**(0.5)))*tmp[j-1]*0.9+P[i])/tmp[j]-1200/(j**(0.5)))

def solve(test):
  N=int(input())
  P=list(map(int,input().split()))
  dp=[-5000]*(N+1)**2
  tmp=[0,1]
  for i in range(N-1):
    tmp.append(tmp[-1]+0.9**(i+1))
  for i in range(N):
    for j in range(i+2):
      dp[(i+1)*(N+1)+j]=max(dp[(i+1)*(N+1)+j],((dp[i*(N+1)+j-1]+1200/((j-1)**(0.5)))*tmp[j-1]*0.9+P[i])/tmp[j]-1200/(j**(0.5)), dp[i*(N+1)+j]) if j>1 else max(dp[(i+1)*(N+1)+j],P[i]-1200,dp[i*(N+1)+j])
  print(max(dp))

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)