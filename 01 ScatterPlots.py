import numpy as np
import matplotlib.pyplot as plt

plt.xlabel('No of persons')
plt.ylabel('No of goods')
plt.title('Data vizualization made easy')
X_data = np.random.random(50) *100    #returns an array
Y_data = np.random.random(50) *100
plt.scatter(X_data,Y_data)
# plt.show()    # displays the data in scatter plot and clears the plot such that new fresh plot can be plotted

plt.xlabel('No of persons')
plt.ylabel('No of goods')
plt.title('Data vizualization made easy')
x_axis = [20,50,20,64,80,90]
y_axis = [55,60,23,45,20,47]
plt.scatter(x_axis,y_axis,c='red', marker='*',alpha=0.3)
plt.show()
 