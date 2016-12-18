import numpy as np
import matplotlib.pyplot as plt
#a = np.array(a)

Pi_array = np.zeros((50,1))
N = list(range(100,5000,200))
Var_array = []
#Var_array = np.zeros((50,1))
for nums in N:
    for k in range(0,50):
        Pi = 0
        a = np.random.uniform(0,1,size=(nums,2))
        for i in range(0,nums):
            if a[i][0] ** 2 + a[i][1] ** 2 <= 1:
                Pi += 1
# Because Pi     Real_Pi
#       ----  = --------
#        100        4

        Pi_array[k] = Pi/(nums/4.0)
#    Var_array.append(np.var(Pi_array))
    Est_var = 0
    mean = np.mean(Pi_array)
    for unit in Pi_array:
        Est_var += (unit - mean)**2
    Var_array.append(Est_var/49.0)

plt.plot(N,Var_array)
plt.title("Sample Variance of the Pi-estimates For Different Values of Samples")
plt.xlabel("Number of Samples")
plt.ylabel("Sample Variance")
plt.show()