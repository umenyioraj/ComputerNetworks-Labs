import random
from networkslab3 import lab3data


def crc_check(a,divisor,Drop=True):
    #crc creation 
    cnt = 0  
    for i in range(0,len(divisor)+1):
        a.append(0)
    print('original data',a)
    print('divisor',divisor)
    tmp_a = a[:]
    i = len(divisor)
    while i < len(a):

        result = [x ^ y for x, y in zip(tmp_a,divisor)]
        print('temp result', result)

    
        # check if result has leading zerores and delete them and append until len == j

        check =  0
        while result[check] != 1 and i < len(a):
            result.pop(0)
            result.append(a[i])
            i+=1

        tmp_a = result[:]
        print('result',result)
            

    result = [x ^ y for x, y in zip(tmp_a,divisor)]
    #print('Last result',result)
 
    while result[0] != 1 and len(result) > len(divisor):
        result.pop(0)
        
    print('remainder!',result)
    remainder = len(result)

    del a[-remainder:]   #delete added zeroes
    a.extend(result)    # add result to end
    print(a)


        


    # bit flip potential

    bfp = []

    for i in range(0,len(a)):
        num = random.randint(0,128)
        bfp.append(num)

    for i in range(len(a)):
        for j in range(len(bfp)):
            if bfp[j] == 8:   #2^7 chance of error
                if a[j] == 0:
                    a[j] = 1
                else:
                    a[j] = 0

    print('BFP arr',bfp)
    
    Drop = True if 8 in bfp else False
    if Drop == True:
        return a, True
    else:
        return a, False
    
    
               

def crc_check2(a,divisor):

    print('original data',a)
    print('divisor',divisor)
    tmp_a = a[:]
    i = len(divisor)
    while i < len(a):

        result = [x ^ y for x, y in zip(tmp_a,divisor)]
        print('temp result', result)


        check =  0
        while result[check] != 1:
            result.pop(0)
            if i < len(a):
                result.append(a[i])
                i+=1

        tmp_a = result[:]
        print('result',result)
            
    if sum(result) != 0:
        result = [x ^ y for x, y in zip(tmp_a,divisor)]
        print('Last result',result)
    seq =[0,1,1,1,0]

    if sum(result) == 0:
        print('No errors detected! Remainder = ', result)
        print('Packet',seq+a+seq)
    else:
        print('Dropped!')
              
test,should_drop = crc_check(lab3data,[1,1,0,0,0,0,0,0,0,1,1,1],Drop=False)

crc_check2(lab3data,[1,1,0,0,0,0,0,0,0,1,1,1])

if should_drop == True:
    print('Should Drop')
else:
    print('No drop')
