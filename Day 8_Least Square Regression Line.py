import statistics

X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]

global mean_X
mean_X = statistics.mean(X)
global mean_Y
mean_Y = statistics.mean(Y)

def pearson_rho(X, Y):
    num = 0
    for i in range(len(X)):
        num += (X[i] - mean_X) * (Y[i] - mean_Y)
    denom = len(X) * statistics.pstdev(X) * statistics.pstdev(Y)
    
    return (num / denom)


def linreg(X, Y):
    """ Returns a tuple of (a,b) for the parameters of regression line: Y = a + b*X """
    
    b = pearson_rho(X, Y) * (statistics.pstdev(Y) / statistics.pstdev(X))
   
    a = mean_Y - (b * mean_X)
    
    return (a, b)


x = 80

y = linreg(X, Y)[0] + linreg(X, Y)[1] * x

print(round(y, 3))