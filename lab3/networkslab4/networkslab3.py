#Getting the layers ready for lab3 portion
import random
arr = []
arr1 = []
arr1trail= [0,0]
arr2 = []
arr3head = [1,0,1,0]
arr3 = []
arr3trail = [1,1,1,1]

# get random 64 bit intger
for i in range(0,64):
   num = random.randrange(0,2)
   arr.append(num)
 
for i in range(0,4):
   arr.insert(0,0)


arr.extend(arr1trail)

arr.insert(0,0)
arr.insert(0,1)
arr.insert(0,0)
arr.insert(0,1)

arr.extend(arr3trail)


#print("Level 4" , arr)

#transmit data

#print('level 3: ', arr)

del arr[:4]
del arr[-4:]

arr2 = arr[:]
lab3data = arr2[:]
#print("Level 2", arr2)

del arr2[:4]
del arr2[-2:]

arr1 = arr2[:]
#print("Level 1", arr1)


#Lab 3 portion
def char_stuff(a):
   beg = 0
   end = 5
   dle_char = 0
   while end <= len(a)+1:
      if a[beg:end] == [0,1,1,1,0]:
         a[beg:beg] = [0,1,1,1,1]
         beg +=10
         end = beg +5
         dle_char +=1
      else:
         end += 1
         beg +=1
   seq = [0,1,1,1,0]
   #print('Char Stuff Transmit',a)

   dle = [0,1,1,1,1]
   beg = 0
   end = 5
   while end < len(a)+1:
      if a[beg:end] == dle and a[beg+5:end+5] == seq:
         a[beg:end] = []
         dle_char -= 1
      else:
         beg +=1
         end +=1
   #print('char stuff recieved',a)
   #print('layer 4:', seq + a + seq)

def bit_stuff(a):
   beg = 0
   end = 3
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

   beg = 0
   end = 4
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


print('Data',lab3data)
print('MSB is digit after the 4 consecutive ones!')
msb = input('Enter MSB: ')
if int(msb) == 1:
   bit_stuff(lab3data)
elif int(msb) == 0:
   char_stuff(lab3data)

