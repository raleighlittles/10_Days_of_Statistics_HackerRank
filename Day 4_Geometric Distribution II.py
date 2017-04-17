# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

user_input = raw_input()
n = input()

def geometric(n, p):
    return math.pow(1-p, n-1) * p

user_input = user_input.split(' ')
p = float(user_input[0]) / float(user_input[1]) 

print round( sum([geometric(x, p) for x in range(1, n+1)]), 3)