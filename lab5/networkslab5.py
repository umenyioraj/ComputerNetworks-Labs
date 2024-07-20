import random

def incr_binary(binary_num):
    if binary_num == '111':
        decimal_num = int(binary_num,2)
        decimal_num = 0
        return bin(decimal_num)[2:].zfill(len(binary_num))
    
    else:
        decimal_num = int(binary_num,2)

        decimal_num +=1
    
        return bin(decimal_num)[2:].zfill(len(binary_num))


def seq_adder(binary_num):
    protocol = [1,0,1]
    arr = []
    row = []
    for j in range(0,64):
        num = random.randrange(0,2)
        row.append(num)
    arr.append(row)
    protocol.extend(row)
    binary_list = [int(bit) for bit in binary_num]
    binary_list.extend(protocol)
    #print('Seq',binary_list)
    return binary_list,binary_num

def bit_stuff(a):
   beg = 6
   end = 9
   seq = [0,1,1,1,0]
   while beg < len(a)-2:
      if a[beg:end] == [0,1,1]:
         if end+1 != len(a) or a[beg:end+2] != seq:
            a.insert(end,0)
            beg = end + 1
            end += 4
      else:
         end +=1
         beg +=1
   #print('Bit Stuff Transmitted',a)

   beg = 6
   end = 10
   while end < len(a) +1:
      
      if a[beg:end] == [0,1,1,0]:
         a.pop(end-1)
         beg = end -1
         end = beg +4
      else:
         beg+=1
         end +=1
   #print('Bit Stuff Recieved', a)
   #print('layer 4:', seq + a + seq)
   return a

def crc_check(a,divisor,Drop=True):
    #crc creation 
    #print('original data',a)  
    for i in range(0,len(divisor)+1):
        a.append(0)
    #print('divisor',divisor)
    tmp_a = a[:]
    i = len(divisor)
    while i < len(a):

        result = [x ^ y for x, y in zip(tmp_a,divisor)]
        #print('temp result', result)

    
        # check if result has leading zerores and delete them and append until len == j

        check =  0
        while result[check] != 1 and i < len(a):
            result.pop(0)
            result.append(a[i])
            i+=1

        tmp_a = result[:]
        #print('result',result)
            

    result = [x ^ y for x, y in zip(tmp_a,divisor)]
    #print('Last result',result)
 
    while result[0] != 1 and len(result) > len(divisor):
        result.pop(0)
        
    #print('remainder!',result)
    remainder = len(result)

    del a[-remainder:]   #delete added zeroes
    a.extend(result)    # add result to end
    #print('seq + remainder',a)


        


    # bit flip potential

    bfp = []

    for i in range(0,len(a)):
        num = random.randint(0,512)
        bfp.append(num)

    for i in range(len(a)):
        for j in range(len(bfp)):
            if bfp[j] == 8:   #2^7 chance of error
                if a[j] == 0:
                    a[j] = 1
                else:
                    a[j] = 0

    #print('BFP arr',bfp)
    
    Drop = True if 8 in bfp else False
    if Drop == True:
        return a, True
    else:
        return a, False

def crc_check2(a,divisor):

    #print('original data',a)
    #print('divisor',divisor)
    tmp_a = a[:]
    i = len(divisor)
    while i < len(a):

        result = [x ^ y for x, y in zip(tmp_a,divisor)]
        #print('temp result', result)


        check =  0
        while result[check] != 1:
            result.pop(0)
            if i < len(a):
                result.append(a[i])
                i+=1

        tmp_a = result[:]
        #print('result',result)
            
    if sum(result) != 0:
        result = [x ^ y for x, y in zip(tmp_a,divisor)]
        #print('Last result',result)
    
    # if sum(result) == 0:
    #     print('No errors detected! Remainder = ', result)
    # else:
    #     print('Dropped!')


binary = '000'
cnt = 1
while cnt < 21:
    a,prev = seq_adder(binary)
    prev_cnt = cnt
    binary = incr_binary(binary)
    bit_stuff_answer = bit_stuff(a)
    crc_answer,should_drop = crc_check(bit_stuff_answer,[1,1,0,0,0,0,0,0,0,1,1,1],Drop=False)
    crc_check2(crc_answer,[1,1,0,0,0,0,0,0,0,1,1,1])
    print('Host A: Packet', cnt , 'Sent')
    if should_drop == True:
        print('Packet', cnt, 'Recived, Dropped due to bit error')
        binary = prev
        cnt = prev_cnt
    
    else:
        num = random.randint(0,25)
        if num == 12:
            print('Packet', cnt, 'Lost')
            binary = prev
            cnt = prev_cnt
        else:
            seq = [0,1,1,1,0]
            print('Host B: Packet', cnt, 'Recieved')
    

            if num == 19:
                print('Host A: Timeout')
                binary = prev
                cnt = prev_cnt
            else:
                print('Host B: ACK', cnt, 'Sent')
                print('Host A: ACK', cnt, 'Recieved')
                print('Final answer', seq + crc_answer + seq)
                cnt +=1

#probably need to add timeouts and other things tbh
 
