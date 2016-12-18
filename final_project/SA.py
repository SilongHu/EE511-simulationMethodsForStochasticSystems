import math
import random
import numpy as np
import matplotlib.pyplot as plt
from deap import benchmarks
try:
    import numpy as np
except:
    exit()

XMAX = 500
YMAX = 500

alpha = 1.1
def Obj(x,y):
    value = 418.9829 * 2 - x * math.sin(math.sqrt(abs(x))) - y * math.sin(math.sqrt(abs(y)))
    return value


value = []
N = 100
MarkovLength = 1000 #Iteration time

allroute_x = []
allroute_y = []

for _ in range(N):

    DecayScale = 0.95
    StepFactor = 0.2 #
    Temperature = 1e5
    Tolerance = 1e-5
    #AcceptPoints = 0.0
    iteration = 0

    route_x = []
    route_y = []
    rnd = random.random()
    # Initial solution: PreBextX, preBestY , Current best value: BestX, BestY
    # Prepared solution: Prex, prey
    PreX = -XMAX * random.random()
    PreY = -YMAX * random.random()

    PreBestX = PreX
    PreBestY = PreY

    PreX = -XMAX * random.random()
    PreY = -YMAX * random.random()

    BestX = PreX
    BestY = PreY

    route_x.append(BestX)
    route_y.append(BestY)
    while Temperature > Tolerance:

        # Choosing the Cooling style
        #Temperature = DecayScale * Temperature #快速降温 For 3.2
        #Temperature = (0.88 ** (iteration + 1) ) * Temperature #Exponential
        #Temperature = Temperature / ( 1 + alpha * math.log( 1 + iteration,math.e)) #logarithmic
        Temperature = Temperature / (1 + 0.1 * iteration) # polynomial
        AcceptPoints = 0.0
        i = 0
        while i < MarkovLength :
            p = 0 # Choose the right range value
            while p == 0:
                NextX = PreX + StepFactor * XMAX * (random.random() - 0.5)
                NextY = PreY + StepFactor * YMAX * (random.random() - 0.5)
                if((NextX >= -XMAX) and (NextX <= XMAX) and (NextY >= -YMAX) and (NextY <= YMAX)):
                    p = 1

            if(Obj(BestX,BestY) > Obj(NextX,NextY)):
                #Preserve the pervious best solution
                PreBestX = BestX
                PreBestY = BestY

                #Update the best solution
                BestX = NextX
                BestY = NextY
                route_x.append(BestX)
                route_y.append(BestY)

                #Metropolis Process
            if (Obj(PreX,PreY) - Obj(NextX,NextY) > 0):
                PreX = NextX
                PreY = NextY
                AcceptPoints += 1
            else:
                changer = -1. * (Obj(NextX,NextY) - Obj(PreX,PreY))/Temperature
                rnd = random.random()
                p1 = math.exp(changer)
                if p1 > rnd:
                    PreX = NextX
                    PreY = NextY
                    AcceptPoints += 1

            i = i + 1
        iteration += 1

    value.append(Obj(BestX,BestY))
    allroute_x.append(route_x[:])
    allroute_y.append(route_y[:])
'''
#*************** Question 3.1 and 3.4 ******************
index = []
for i in range(N):
    if value[i] < 0.1:
        index.append(i)
print (index)
ki = {}
#it belongs to minimum value, then find minimum route length
for it in index:
    ki[it] = len(allroute_y[it])

print (ki)
a = min(ki, key=ki.get)
k = len(allroute_y[a])

X = np.arange(-500, 500, 10)
Y = np.arange(-500, 500, 10)
X, Y = np.meshgrid(X, Y)
Z = np.zeros(X.shape)
def schwefel_arg0(sol):
    return benchmarks.schwefel(sol)[0]

for i in range(X.shape[0]):
    for j in range(X.shape[1]):

        Z[i, j] = schwefel_arg0((X[i, j], Y[i, j]))

plt.figure()
contour = plt.contour(X, Y, Z)
plt.colorbar(contour)
plt.title('Scwefel Contours Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(allroute_x[a],allroute_y[a],'ob')
#plt.plot(allroute_x[a][0:int (k/3)],allroute_y[a][0:int(k/3)],'ow')
#plt.plot(allroute_x[a][int(k/3):int( 2 * k/3)],allroute_y[a][int(k/3):int( 2 * k/3)],'^b')
#plt.plot(allroute_x[a][int(2 * k/3):],allroute_y[a][int(2 * k/3):],'*k')
plt.show()


#********************************************************
'''

#*************** Question 3.3 Start **************************
plt.figure()
axes = plt.gca()
#axes.set_xlim([0,1400])
#axes.set_ylim([0,30])
plt.hist(value,bins = 40)
plt.xlabel('Converge minimum value')
plt.ylabel('Frequency of corresponding minimum value')
str = "Polynomial Cooling Schedule with "+str(MarkovLength)+ " Iterations"
#str = "Logarithmic Cooling Schedule with "+str(MarkovLength)+ " Iterations"
#str = "Exponential Cooling Schedule with "+str(MarkovLength)+ " Iterations"
plt.title(str)
plt.show()

#*************** Question 3.3 End **************************
