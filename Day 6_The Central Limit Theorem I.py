# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

max_weight = input()
num_boxes = input()
avg = input()
std_dev = input()

sample_avg = num_boxes * avg
sample_std_dev = math.sqrt(num_boxes) * std_dev

def cdf(avg, std_dev, x):
    inner = 1 + math.erf((x - avg) / (std_dev * math.sqrt(2)))
    return 0.5 * inner

ans = cdf(num_boxes * avg, math.sqrt(num_boxes) * std_dev, 9800)
print round(ans, 4)