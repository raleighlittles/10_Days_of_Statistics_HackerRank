# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def geometric(n, p):
    return math.pow(1-p, n-1) * p

user_input = raw_input()
n = input()
user_input = user_input.split(' ')
p = float(user_input[0]) / float(user_input[1])

print round(geometric(n, p), 3)