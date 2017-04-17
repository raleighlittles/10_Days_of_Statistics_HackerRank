# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def cdf(std_dev, avg, x):
    inner = 1 + math.erf((x - avg) / (std_dev * math.sqrt(2)))
    return 0.5 * inner

parameters = raw_input()
score = input()
passing_score = input()

parameters = parameters.split(' ')
avg, std_dev = int(parameters[0]), int(parameters[1])

ans_1 = 1 - cdf(std_dev, avg, score)
ans_2 = 1 - cdf(std_dev, avg, passing_score)
ans_3 = cdf(std_dev, avg, passing_score)

print round(ans_1 * 100, 2)
print round(ans_2 * 100, 2)
print round(ans_3 * 100, 2)