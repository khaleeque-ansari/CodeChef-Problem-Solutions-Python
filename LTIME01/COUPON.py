import sys

t = input()

for z in xrange(t):
    m,n = map(int,sys.stdin.readline().split())
    pri = []
    dis = []

    for zz in xrange(m):
        pri.append(map(int,sys.stdin.readline().split()))
    for zzz in xrange(m):
        dis.append(map(int,sys.stdin.readline().split()))

    la = 0
    path = 0
    if m == 2:
        for i in xrange(n):
            if i == 0:
                if pri[0][0] < pri[1][0]:
                    la = la + pri[0][0]
                else:
                    la = la + pri[1][0]
                    path = 1
            else:
                if path == 0:
                    if max(pri[0][i]-dis[0][i-1],0) < pri[1][i]:
                        la = la + max(pri[0][i]-dis[0][i-1],0)
                    else:
                        la = la + pri[1][i]
                        path = 1
                else:
                    if max(pri[1][i]-dis[1][i-1],0) < pri[0][i]:
                        la = la + max(pri[1][i]-dis[1][i-1],0)
                    else:
                        la = la + pri[0][i]
                        path = 0


    print la                        
                        


    


