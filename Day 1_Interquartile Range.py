# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = int(raw_input())
elements = raw_input()
elements = elements.split(' ')
frequencies = raw_input()
frequencies = frequencies.split(' ')

data = []
for i in range(len(frequencies)):
    for j in range(int(frequencies[i])):
        data.append(int(elements[i]))
        
        
data = sorted(data)
#print data
#print len(data)
if len(data) % 2 == 0:
    data_1 = data[0: (len(data) // 2)]
    data_2 = data[(len(data) // 2): ]

else:
    data_1 = data[0 : int((len(data)/2))]
    data_2 = data[int((len(data)/2)) + 1 : ]

def median(my_list):
    index = len(my_list) // 2
    
    if len(my_list) % 2 != 0:
        return my_list[index]
    
    return (my_list[index] + my_list[index-1]) / 2

#print data_1
#print data_2
mid_1 = median(data_1)
mid_2 = median(data_2)
#print mid_1, mid_2
print (float(mid_2 - mid_1))

