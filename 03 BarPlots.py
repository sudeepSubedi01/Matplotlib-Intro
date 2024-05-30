import numpy as np
import matplotlib.pyplot as plt

plt.title('Survey of people liking different fruits')
plt.xlabel('Fruits')
plt.ylabel('No of people')
x = ['Mango','Apple','Banana','Pineapple','Grape']
y = [55,20,56,36,20]

plt.bar(x,y,color='g',align='edge',width=0.5,edgecolor='black')
plt.show()