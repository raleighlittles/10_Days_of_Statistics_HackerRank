# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

means = raw_input()
means = means.split(' ')
mean_a, mean_b = float(means[0]), float(means[1])

def poisson(k, lam):
    return (math.pow(lam, k) * math.pow(math.e, -1 * lam)) / math.factorial(k)

cost_a = lambda x: 160 + 40 * (x ** 2)
cost_b = lambda y: 128 + 40 * (y ** 2)

expected_a = sum([cost_a(x) * poisson(x, mean_a) for x in range(0, 10+1)])
expected_b = sum([cost_b(y) * poisson(y, mean_b) for y in range(0, 10+1)])

print round(expected_a, 3)
print round(expected_b, 3)