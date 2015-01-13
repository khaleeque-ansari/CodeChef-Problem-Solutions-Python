
finstr = ''
sc = '0110100110010110'      
sn = '1001011001101001'
for c in sc:
    if c == '0':
        finstr +=sc
    if c == '1':
        finstr +=sn

for n in sn:
    if n == '0':
        finstr +=sc
    if n == '1':
        finstr +=sn

#print len(finstr)
ffinstr = finstr        

cases = int(raw_input())

for i in range(0,cases):
    lenSeq = int(raw_input())

    temp = lenSeq/512

    for i in range(0,temp+1):
        ffinstr += finstr


    str2 = raw_input()
    str2 = str2.replace(" ", "")


    for i in range(1,lenSeq + 1):
        substr = str2[:i]
        print ffinstr.find(substr),
    
