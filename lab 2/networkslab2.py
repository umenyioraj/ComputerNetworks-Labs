import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

data = [1,1,1,0,0,0,0,1,0,1,0,1]

proccesed_data = [-5 if val == 0 else 5 for val in data]  
plt.step(range(len(proccesed_data)), proccesed_data)
plt.grid(True)
plt.xlabel('Time (milliseconds)')
plt.ylabel('Signal')
plt.title('NRZ Encoding')
plt.show()

toggle_data = []
prev = 0
for val in data:
   if val == 0:
      toggle_data.append(0)
   elif val == 1:
      if prev == 1: # prev 1 was a 5
         toggle_data.append(0)
         prev = 0
      else:
         toggle_data.append(5)
         prev = 1
print(toggle_data)
plt.step(range(len(toggle_data)), toggle_data)
plt.ylim(0,10)
plt.xlim(-1,12)
plt.xlabel('Time (milliseconds)')
plt.ylabel('Signal')
plt.title('NRZI Encoding')
plt.show()

manchester_data = []
for bit in data:
    if bit == 1:
        manchester_data.extend([1, -1])
    else:
        manchester_data.extend([-1, 1])

processed_data = np.repeat(manchester_data, 2)
time_reference = np.arange(len(processed_data)) * 1

plt.step(time_reference, processed_data)
plt.xlabel('Time (milliseconds)')
plt.ylabel('Signal')
plt.title('Manchester Encoding')
plt.grid(True)
plt.show()
      
data_length = 16
data = [random.randint(0,1) for _ in range(data_length)]
print('orginal data',data)
n = 4
a = 0
while n < len(data)+1:
   if data[a:n] == [0,0,0,0]:
      data[a:n] = [1,1,1,1,0]
   elif data[a:n] == [0,0,0,1]:
      data[a:n] = [0,1,0,0,1]
   elif data[a:n] == [0,0,1,0]:
      data[a:n] = [1,0,1,0,0]
   elif data[a:n] == [0,0,1,1]:
      data[a:n] = [1,0,1,0,1]
   elif data[a:n] == [0,1,0,0]:
      data[a:n] = [0,1,0,1,0]
   elif data[a:n] == [0,1,0,1]:
      data[a:n] = [0,1,0,1,1]
   elif data[a:n] == [0,1,1,0]:
      data[a:n] = [0,1,1,1,0]
   elif data[a:n] == [0,1,1,1]:
      data[a:n] = [0,1,1,1,1]
   elif data[a:n] == [1,0,0,0]:
      data[a:n] = [1,0,0,1,0]
   elif data[a:n] == [1,0,0,1]:
      data[a:n] = [1,0,0,1,1]
   elif data[a:n] == [1,0,1,0]:
      data[a:n] = [1,0,1,1,0]
   elif data[a:n] == [1,0,1,1]:
      data[a:n] = [1,0,1,1,1]
   elif data[a:n] == [1,1,0,0]:
      data[a:n] = [1,1,0,1,0]
   elif data[a:n] == [1,1,0,1]:
      data[a:n] = [1,1,0,1,1]
   elif data[a:n] == [1,1,1,0]:
      data[a:n] = [1,1,1,0,0]
   elif data[a:n] == [1,1,1,1]:
      data[a:n] = [1,1,1,0,1]
   a += 5
   n = a +4
print('4B/5B data', data)

plt.step(range(len(data)), data)
plt.grid(True)
plt.xlim(0,16)
plt.xlabel('Time (milliseconds)')
plt.ylabel('Signal')
plt.title('4B/5BEncoding')
plt.show()