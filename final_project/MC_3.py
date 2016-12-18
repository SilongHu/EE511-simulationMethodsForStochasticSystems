import random
import numpy as np

def integrateMC(func, dim, limit, expected, N):
    I = 1. / N
    tol = []
    for n in range(dim):
        I *= (limit[n][1] - limit[n][0])

    for k in range(N):
        x = []
        for n in range(dim):
            x.append(random.uniform(limit[n][0], limit[n][1]))
        tol.append(func(x))
    est_var = 0
    m = np.mean(tol)
    for nums in tol:
        est_var += (nums - m) ** 2

    return I * np.sum(tol), abs(I * np.sum(tol) - expected), est_var * I / (N - 1)

def integrand(x):
    return (abs(4*x[0] - 2) * abs(4*x[1] - 2))

def sampler():
    while True:
        y = random.uniform(0.,1.)
        x = random.uniform(0.,1.)
        yield (x,y)

dim, limit = 2, [[0, 1], [0, 1]]
N = 100  # starting value for number of MC samples
x, y, y2 = [], [], []  # for plotting
n = 2  # the number of times each integration is performed to
# define average and SDOM

domainsize = 1 # x,y belongs to [0,1]
expected = 1 # Calculate the integal value of g(x,y)
for nmc in [50, 100, 500, 1000]:
    random.seed(1)
    result, error,est_var = integrateMC(integrand, dim,limit,expected, nmc)
    #diff = abs(result - expected)
    print ("Using n = ", nmc)
    print ("Result = ", result, "estimated variance = ", est_var)
    print ("Known result = ", expected, " error = ", error, " = ", 100.* error/expected, "%")
    print (" ")