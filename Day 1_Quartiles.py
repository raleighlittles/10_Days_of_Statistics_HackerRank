# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = raw_input()
data = raw_input()
data = data.split(' ')
data = [int(i) for i in data]
data = sorted(data)

if len(data) % 2 == 0:
    data_1 = data[0 : (len(data) // 2)]
    data_2 = data[(len(data) // 2) : ]
    
else:
    data_1 = data[0: int(math.floor(len(data)/2))]
    data_2 = data[int(math.floor(len(data)/2)) + 1 : ]
    
def median(my_list):
    index = len(my_list) // 2
    
    if len(my_list) % 2 != 0:
        return my_list[index]
    
    return (my_list[index] + my_list[index-1]) / 2

#print data
print median(data_1)
print median(data)
print median(data_2)
