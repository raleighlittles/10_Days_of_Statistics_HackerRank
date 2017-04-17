n = int(input())
X = [float(x) for x in input().split()]
Y = [float(x) for x in input().split()]

X_rank = [sorted(X).index(x) + 1 for x in X]
Y_rank = [sorted(Y).index(y) + 1 for y in Y]

diff_sq = [(x - y) ** 2 for (x, y) in zip(X_rank, Y_rank)]
coeff = 1 - (6 * sum(diff_sq)) / (n**3 - n)

print(round(coeff, 3))