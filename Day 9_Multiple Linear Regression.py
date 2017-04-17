# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn import linear_model

m,n = raw_input().split()
inputs = []
for i in range(int(n)):
    inputs.append([float(j) for j in raw_input().split()])
    
y = [x.pop() for x in inputs]
f = input() # Record the number of 'features' that you will apply the linear model to!
x = []
for k in range(f): # The next series of inputs are the values of x1, x2 to be used later
    x.append([float(l) for l in raw_input().split()])

lm = linear_model.LinearRegression()
lm.fit(inputs, y)
a = lm.intercept_
b = lm.coef_

for m in range(0, len(x)):
    out = a + x[m][0] * b[0] + x[m][1] * b[1]
    print out

    

