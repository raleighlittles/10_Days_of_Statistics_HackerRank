# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def poisson(k, lam):
    return (math.pow(lam, k) * math.pow(math.e, -1*lam)) / math.factorial(k)

lam = input()
k = input()

print poisson(k, lam)