from collections import defaultdict
a_grp, b_grp = [],[]
n, m = map(int,input().split())
A = defaultdict(list)
B = []

for i in range(n):
    A[input()].append(i)

for j in range(m):
    B.append(input())

a_grp = list(A)

for i in range(len(B)):
    if(B[i] in a_grp):
        for x in A[B[i]]:
            print(x+1,end = ' ')
        print()
    else:
        print(-1)