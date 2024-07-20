import random
arr = []
arr1 = []
arr1trail= [0,0]
arr2 = []
arr3head = [1,0,1,0]
arr3 = []
arr3trail = [1,1,1,1]

for i in range(0,16):
   num = random.randrange(0,2)
   arr.append(num)

for i in range(0,4):
   arr.insert(0,0)
#print(arr)

arr.extend(arr1trail)
#print(arr)

arr.insert(0,0)
arr.insert(0,1)
arr.insert(0,0)
arr.insert(0,1)

arr.extend(arr3trail)

print("Level 4" , arr)



#transmit data

for i in arr:
   arr3.append(i)
print("Level 3", arr3)
#print(len(arr3))

for i in range(len(arr)):
   if i in range(4,26):
      arr2.append(arr[i])
print("Level 2", arr2)
#print(len(arr2))

for i in range(len(arr2)):
   if i in range(4,20):
      arr1.append(arr2[i])
print("Level 1", arr1)
#print(len(arr1))



   
      

   
   
