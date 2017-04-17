# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()

elements = raw_input()
int_elements = []
# Store elements string into an array where each number is a spot in the array
for elem in elements.split(' '):
    int_elements.append(int(elem))

    
sum_of_elements = sum(int_elements)
mean = sum_of_elements / float(n)
print mean

sorted_elements = sorted(int_elements)

middle_elements = [sorted_elements[int(n)/2], sorted_elements[int(n)/2 - 1]]

median_of_elements = sum(middle_elements) / 2.0

print float(median_of_elements)

highest_freq, highest_freq_elem = 0, 0
for elem in sorted_elements:
    current_count = sorted_elements.count(elem)
    if (current_count > highest_freq):
        highest_freq = current_count
        highest_freq_elem = elem
        
mode = highest_freq_elem
print mode
        


