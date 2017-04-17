# Enter your code here. Read input from STDIN. Print output to STDOUT

import statistics

n = input()
X = input()
Y = input()

X, Y = X.split(' '), Y.split( ' ')
X.pop()
X = [float(x) for x in X]
Y = [float(y) for y in Y]

def pearson_rho(X, Y):
    mean_X, mean_Y = statistics.mean(X), statistics.mean(Y)
    stddev_X, stddev_Y = statistics.pstdev(X), statistics.pstdev(Y)
    num = 0
    for i in range(0, len(X)):
        num += (X[i] - mean_X) * (Y[i] - mean_Y)
        
    denom = len(X) * stddev_X * stddev_Y
    
    return (num / denom)

print (round(pearson_rho(X, Y), 3))
        
    