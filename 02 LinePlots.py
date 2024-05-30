import numpy as np
import matplotlib.pyplot as plt

years = [(2006+x+2) for x in range(16)]
# print(years)
weights = [50,60,20,46,47,89,36,23,45,12,69,46,43,25,68,95]
# print(weights)
plt.scatter(years,weights)
plt.show()
plt.plot(years,weights,c='r',linestyle='--',lw=2)
# plt.plot(years,weights,lw=2, 'r--')
plt.show()