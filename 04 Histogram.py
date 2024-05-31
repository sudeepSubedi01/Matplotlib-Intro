import numpy as np
import matplotlib.pyplot as plt

ages = np.random.normal(20,1.5,1000)    #normal distribution with mean=20, sd=1.5, no of data=1000
print(len(ages))
plt.hist(ages,
        #  bins=[ages.min(),18,21,21,ages.max()],
        bins =20,
        cumulative=True
         
         )
plt.show()
