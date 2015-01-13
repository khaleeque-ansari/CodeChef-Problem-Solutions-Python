import sys
n=int(raw_input())

for i in range(n):
    str = raw_input()
    hole = 0
    for c in str:
        if c == 'B':
            hole += 2
        elif c in ['A','D','O','P','Q','R',]:
            hole += 1
        else:
            pass
    print hole

        
        
        
    
            
        
        


