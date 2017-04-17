# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()

elements = raw_input()
weights = raw_input()

elements = elements.split(' ')
weights = weights.split(' ')

numerator = 0
denominator = 0

for i in range(0, len(elements)):
    numerator = numerator + int(weights[i]) * int(elements[i])
    denominator = denominator + int(weights[i])


weighted_mean = numerator / float(denominator)
print round(weighted_mean, 1)
