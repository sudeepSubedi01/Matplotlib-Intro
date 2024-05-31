import matplotlib.pyplot as plt
import numpy as np

langs = ['Python','C++','Java','C#','Ruby']
votes = [ 25,5,45,63,45]
explodes = [0,1,0,0.5,0]

plt.pie(votes, labels = langs, explode = explodes,autopct='%.2f%%',pctdistance=1.5, startangle= 90)
plt.show()