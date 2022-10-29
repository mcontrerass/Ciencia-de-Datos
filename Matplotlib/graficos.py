import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(1,150,200)
y = x + x**2
#print(x)
#print(y)
plt.plot(x,y,'blue')
plt.title('Gráfico números al cuadrado')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y (x al cuadrado)')
plt.show()

# subplots
plt.subplot(1,2,1)
plt.plot(x,y,'g')
plt.subplot(1,2,2)
plt.plot(x,y,'r')
plt.show()

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
men_std = [2, 3, 4, 1, 2]
women_std = [3, 5, 2, 3, 3]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, men_means, width, yerr=men_std, label='Men')
ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
       label='Women')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

plt.show()