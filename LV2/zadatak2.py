import numpy as np
import matplotlib . pyplot as plt

data=np.loadtxt("data.csv", delimiter=",", dtype=float, skiprows=1)

#a
print(data.shape[0])

#b
plt . scatter (data[:,1], data[:,2], s=1)
plt.show()

#c
plt . scatter (data[::50,1], data[::50,2], s=1)
plt.show()

#d
print(min(data[:,1]))
print(max(data[:,1]))
print(np.mean(data[:,1]))

#e
men = data[np.where(data[:,0] == 1)]
women = data[np.where(data[:,0] == 0)]
men = men[:,1]
women = women[:,1]

print(min(men))
print(max(men))
print(np.mean(men))


print(min(women))
print(max(women))
print(np.mean(women))


