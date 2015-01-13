import sys
###########
# prime numbers are only divisible by unity and themselves
# (1 is not considered a prime number by convention)
def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
# test ...




###########

t = input()

for z in xrange(t):
    n = input()
    nums = map(int,sys.stdin.readline().split())

    mn =  max(nums)
    
    pl = []
    for i in range(2,mn+1):
        if isprime(i):
            pl.append(i)
    #print pl

    ll = []

    for j in xrange(len(pl)):
        ll.append(0)
    
    for ii in nums:
        counter = 0
        loop=2
        while loop<=ii and counter <= len(pl):
            if ii%loop==0:
                ii/=loop
                ll[counter] +=1
            else:
                counter +=1 
                loop = pl[counter]

    prod = 1
    for i in ll :
        prod *= (i+1)

    print prod
        

        
        
    
