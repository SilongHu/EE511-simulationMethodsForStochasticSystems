from __future__ import division
import numpy as np
import random
import scipy.interpolate as interpolate
import math
import matplotlib.pyplot as plt
from scipy.stats import norm

def inverse_transform_sampling(data, n_bins=50, n_samples=1000):
    hist, bin_edges = np.histogram(data, bins=n_bins, density=True)
    cum_values = np.zeros(bin_edges.shape)
    cum_values[1:] = np.cumsum(hist*np.diff(bin_edges))
    inv_cdf = interpolate.interp1d(cum_values, bin_edges)
    r = np.random.rand(n_samples)
    return inv_cdf(r)

def f_a(x):
    return math.exp(5 * abs(x[0] - 0.5) + 5 * abs(x[1] - 0.5))

def f_b(x):
    return math.cos(math.pi + 5 * (x[0] + x[1]))

def f_c(x):
    """ integrand function """
    return (abs(4 * x[0] - 2) * abs(4 * x[1] - 2))

def integrateMC(func, dim, limit, N):
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
    return I * np.sum(tol), est_var * I / (N - 1)

def integrate(func, dim, limit, N):
    I = 1. / N
    tol = []
    for n in range(dim):
        #print (limit[n][1])
        I *= (limit[n][1] - limit[n][0])

    for k in range(N):
        x = []
        for n in range(dim):
            x.append(random.uniform(limit[n][0], limit[n][1]))
        #print ("x: ",x)
        #print ('func: ',func(x))
        tol.append(func(x))
    return tol


u1 = []
u2 = []
tol = []
dim = 2
limit_a = [[0, 1], [0, 1]]
limit_b = [[-1, 1], [-1, 1]]
limit_c = [[0, 1], [0, 1]]
N = 1000  # starting value for number of MC samples


#********************* Function A Operation ************
## Let's try 1-D formula:

def g_a1(x):
    return  0.792 * 2.5 **(abs(x[0] - 0.5))

def f_a1(x):
    return math.exp(5 * abs(x[0] - 0.5))

data_a = integrate(g_a1, dim, limit_a, N)
#print ("g_a1 integral value: ",np.mean(data_a))

g_dista = inverse_transform_sampling(data_a,50,1000)
ua = []
for i in range(1000):
    ua.append(random.random())
g_dista = g_dista * ua
h_a = []
for items in g_dista:
    h_a.append(f_a1([items])/g_a1([items]))

data_a1 = integrate(g_a1, dim, limit_a, N)
g_dista1 = inverse_transform_sampling(data_a1,50,1000)
ua1 = []
for i in range(1000):
    ua1.append(random.random())

g_dista1 = g_dista1 * ua1
h_a1 = []
for items in g_dista1:
    h_a1.append(f_a1([items])/g_a1([items]))

h_a = np.array(h_a) * np.array(h_a1)
print ('Importance Sampling Value of A: ', np.mean(h_a),' Estimate variance of IS of A: ',np.var(h_a)/N)

v_a = integrateMC(f_a, dim, limit_a, N)
print ("MC integral a:", v_a[0], "MC estimate variance of a: ",v_a[1])
#*************************************************************


#********************* Function B Operation ******************
#Separate Cos(-Pi + 5(x + y)) = -Cos(5x)Cos(5y) + Sin(5x)Sin(5y)
def g_b1(x):
    return 2.93 /math.sqrt(2 * math.pi * 1) * math.exp( - x[0] ** 2/ 2)

def g_b2(x):
    return 2.93 / math.sqrt(2 * math.pi * 1) * math.exp(- x[0] ** 2 / 2)

def f_b1(x):
    return math.cos(5 * x[0])

def f_b2(x):
    return math.sin(5 * x[0])

    # The Cos part
data_b1 = integrate(g_b1, dim, limit_b, N)
#print ("g_a1 integral value: ",np.mean(data_b1))


g_distb1 = inverse_transform_sampling(data_b1,50,1000)
ub1 = []
for i in range(1000):
    ub1.append(random.random())
g_distb1 = g_distb1 * ub1
h_b1 = []
for items in g_distb1:
    h_b1.append(f_b1([items])/g_b1([items]))

g_distb11 = inverse_transform_sampling(data_b1,50,1000)
ub11 = []
for i in range(1000):
    ub11.append(random.random())
g_distb11 = g_distb11 * ub11
h_b11 = []
for items in g_distb11:
    h_b11.append(f_b1([items])/g_b1([items]))

h_b1 = np.array(h_b1) * np.array(h_b11)

# The Sin part
data_b2 = integrate(g_b2, dim, limit_b, N)
#print ("g_a1 integral value: ",np.mean(data_b1))
g_distb2 = inverse_transform_sampling(data_b2, 50, 1000)
ub2 = []
for i in range(1000):
    ub2.append(random.random())
g_distb2 = g_distb2 * ub2
h_b2 = []
for items in g_distb2:
    h_b2.append(f_b2([items]) / g_b2([items]))

g_distb21 = inverse_transform_sampling(data_b2, 50, 1000)
ub21 = []
for i in range(1000):
    ub21.append(random.random())
g_distb21 = g_distb21 * ub21
h_b21 = []
for items in g_distb21:
    h_b21.append(f_b2([items]) / g_b2([items]))

h_b2 = np.array(h_b2) * np.array(h_b21)

print ('Importance Sampling Value of B: ', np.mean(-h_b1 + h_b2),' Estimate variance of IS of B: ',np.var(-h_b1 + h_b2)/N)

v_b = integrateMC(f_b, dim, limit_a, N)
print ("MC integral b:", v_b[0], "MC estimate variance of b: ",v_b[1])
#*************************************************************

#********************* Function C Operation *******************
def g_c1(x):
    return  -1. * (x[0] - 1) ** 2 + 1.33

def f_c1(x):
    return abs(4 * x[0] - 2)

data_c = integrate(g_c1, dim, limit_c, N)
#print ("g_c1 integral value: ",np.mean(data_c))

g_distc = inverse_transform_sampling(data_c,50,1000)
uc = []
for i in range(1000):
    uc.append(random.random())
g_distc = g_distc * uc
h_c = []
for items in g_distc:
    h_c.append(f_c1([items])/g_c1([items]))

data_c1 = integrate(g_c1, dim, limit_c, N)
g_distc1 = inverse_transform_sampling(data_c1,50,1000)
uc1 = []
for i in range(1000):
    uc1.append(random.random())

g_distc1 = g_distc1 * uc1
h_c1 = []
for items in g_distc1:
    h_c1.append(f_c1([items])/g_c1([items]))

h_c = np.array(h_c) * np.array(h_c1)
print ('Importance Sampling Value of C: ', np.mean(h_c),' Estimate variance of IS of C: ',np.var(h_c)/N)

v_c = integrateMC(f_c, dim, limit_c, N)
print ("MC integral c:", v_c[0], "MC estimate variance of c: ",v_c[1])
#*************************************************************
