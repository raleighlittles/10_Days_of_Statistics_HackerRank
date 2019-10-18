# Enter your code here. Read input from STDIN. Print output to STDOUT
# import math

# def cdf(std, avg, x):
#     inner = 1 + math.erf((x-avg) / (std * math.sqrt(2)))
#     return 0.5 * inner

# inputs = raw_input()
# input_single = input()
# input_range = raw_input()

# inputs = inputs.split(' ')
# input_range = input_range.split(' ')

# ans_1 =  cdf(int(inputs[1]), int(inputs[0]), input_single)

# ans_2 = cdf(int(inputs[1]), int(inputs[0]), int(input_range[1])) - cdf(int(inputs[1]), int(inputs[0]), int(input_range[0]))

# print round(ans_1, 3)
# print round(ans_2, 3)

# Import library
import math

# Define functions
def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

# Set data
initial_values = list(map(float, input().split()))
mean = initial_values[0]
std = initial_values[1]
less_period = float(input())
between_period = list(map(float, input().split()))

# Gets the result and show on the screen
print (round(cumulative(mean, std, less_period),3))
print (round(cumulative(mean, std, between_period[1]) - cumulative(mean, std, between_period[0]), 3))