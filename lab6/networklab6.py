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
   end = 9
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
#do a for loop that adds first three packets to the matrix
#do all checks for all three packs one at a time
#hand off to next level one at a time if they all are sent
#ack the last good packet in order and buffer the one next in line and dont send up to next level yet
matrix = []
#created 20 packets
for i in range(0,20):
    a,prev = seq_adder(binary)
    binary = incr_binary(prev)
    matrix.append(a)
#print(matrix)

#sliding window implementation
k=3
cnt = 0
res_matrix = [[]] * len(matrix)
saved_res = [[]] * len(matrix) #will use if I need to output packet instead
for i in range(0,len(matrix),k):
    curr_list = matrix[i:i+k]   #gets the first three packets
    for sublist in curr_list:   #splits each packet down to one at a time                           
            #print('sublist',sublist)
            bit_stuff_answer = bit_stuff(sublist)
            crc_answer,should_drop = crc_check(bit_stuff_answer,[1,1,0,0,0,0,0,0,0,1,1,1],Drop=False)
            crc_check2(crc_answer,[1,1,0,0,0,0,0,0,0,1,1,1])
            #print('Host A: Packet', cnt , 'Sent') 
            if should_drop == True:
                #('Packet', cnt, 'Recived, Dropped due to bit error')
                res_matrix[cnt] = ["Error"]
                saved_res[cnt] = sublist[:]
                cnt +=1 
            
            else:
                num = random.randint(0,25) 
                if num == 12: #packet lost chance
                    res_matrix[cnt] = ["Error"]
                    saved_res[cnt] = sublist[:]
                    cnt+=1
                    
                elif num == 19: #timeout occured chance
                    res_matrix[cnt] = ["Error"]
                    saved_res[cnt] = sublist[:]
                    cnt+=1

                elif res_matrix[cnt-1] == ["Error"] or res_matrix[cnt-2]== ['Error']: #prev packet lost
                    res_matrix[cnt] = 'Buffer'
                    saved_res[cnt] = sublist[:]
                    cnt+=1

                else: #prev packet had no errors
                    res_matrix[cnt] = 'Packet Done'
                    #print('Final answer', seq + crc_answer + seq)
                    if cnt < 19:
                        cnt +=1
    print(res_matrix)

    if ['Error'] in res_matrix:
        index = res_matrix.index(["Error"])
        j = index
        end = index + 2
        while j < end: 
            curr_list = matrix[j:j+k]
            for sublist in curr_list:
                bit_stuff_answer = bit_stuff(sublist)
                crc_answer,should_drop = crc_check(bit_stuff_answer,[1,1,0,0,0,0,0,0,0,1,1,1],Drop=False)
                crc_check2(crc_answer,[1,1,0,0,0,0,0,0,0,1,1,1])
                if should_drop == True:
                    #('Packet', cnt, 'Recived, Dropped due to bit error') Error Move on
                    res_matrix[j] = ["Error"]
                    
                else:
                    num = random.randint(0,25) 
                    if num == 12: #packet lost chance
                        res_matrix[j] = ["Error"]
                            
                    else:
                        num = random.randint(0,25)
                        if num == 19: #timeout occured chance (ack lost)
                            res_matrix[j] = ["Error"]

                        else:
                            res_matrix[j] = 'Packet Done'                                   
                            print('Error Check',res_matrix)
                        j+=1
                            

