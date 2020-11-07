# QUESTION 15

# Importing pips
import matplotlib.pyplot as plt
import numpy as np

# Defining X and Y axis
n=int(input())
z=0

x = np.arange (-50, 50)
for i in range (1, n+1):
    z=z+(2/(i*np.pi))*((-1)^(i+1))*(np.sin(2*np.pi*i*50*x))
plt.plot(x,z)
plt.show()
