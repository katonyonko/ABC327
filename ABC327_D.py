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
3 2
1 2
2 3
3 3
1 2 3
2 3 1
10 1
1
1
7 8
1 6 2 7 5 4 2 2
3 2 7 2 1 2 3 3
"""

def solve(test):
  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  ans='Yes'
  G=[set() for _ in range(N)]
  for i in range(M):
    G[A[i]-1].add(B[i]-1)
    G[B[i]-1].add(A[i]-1)
  num=[-1]*N
  for i in range(N):
    if num[i]==-1:
      num[i]=0
    else: continue
    q=deque([i])
    while q:
      x=q.popleft()
      for j in G[x]:
        if num[j]==-1:
          num[j]=num[x]^1
          q.append(j)
        else:
          if num[j]!=num[x]^1:
            ans='No'
            break
    if ans=='No':
      break
  if test==0:
    print(ans)
  else:
    return None

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