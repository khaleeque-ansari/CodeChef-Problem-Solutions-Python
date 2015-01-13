
amount, balance = [float(x) for x in raw_input().split()]

if amount%5 != 0:
    print '%.2f' %balance
elif amount > balance - 0.50:
    print '%.2f' %balance
else :
    print '%.2f' % (balance - amount - 0.50)
        
        
    

    
