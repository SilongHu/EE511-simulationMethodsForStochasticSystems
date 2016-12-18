import numpy as np
import matplotlib.pyplot as plt

Pi_array = np.zeros((50,1))
for k in range(0,50):
    Pi = 0
    a = np.random.uniform(0,1,size=(100,2))
    for i in range(0,100):
        if a[i][0] ** 2 + a[i][1] ** 2 <= 1:
            Pi += 1
# Because Pi     Real_Pi
#       ----  = --------
#        100        4

    Pi_array[k] = Pi/25.0

plt.hist(Pi_array)  # plt.hist passes it's arguments to np.histogram
plt.title("Histogram of 50 Pi-Estimate")
plt.xlabel("Pi Estimate Value")
plt.ylabel("Frequency")
plt.show()