# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

average = 500
std_dev = 80

print 500 - 1.96 * (std_dev / math.sqrt(100))
print 500 + 1.96 * (std_dev / math.sqrt(100))