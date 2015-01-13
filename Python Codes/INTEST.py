import sys

n,k = map(int,sys.stdin.readline().split(" "))

array=map(int,sys.stdin.readlines())


count = 0
for i in array:
    if i%k == 0 :
        count += 1
print count


    


