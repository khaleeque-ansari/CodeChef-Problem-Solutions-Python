cases = int(raw_input())

for i in range(0,cases):
    num = int(raw_input())
    ans = 0

    while num != 0:
        ans += num/5
        num = num/5
        
    print ans
    


