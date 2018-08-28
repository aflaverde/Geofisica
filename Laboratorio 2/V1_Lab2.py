
# coding: utf-8

# In[11]:


get_ipython().run_line_magic('pylab', 'inline')
import numpy as np
import math
from scipy.interpolate import InterpolatedUnivariateSpline


# In[12]:


G=6.67e-11
pi=np.pi
roS=2700

x = [0, 623, 1246, 1869, 2492, 3115, 3738, 4361, 4984, 5607, 6230, 6853]
bou = [0.035, -0.263, 1.010, 2.985, 5.816, 8.778, 8.245, 8.569, 8.237, 7.423, 6.547, 4.937]

plt.plot(x, bou)
plt.grid()
plt.title('Anomalía de Bouguer vs Distancia')
plt.xlabel('X (m)')
plt.ylabel('Anomalia de bouger (mGal)')


# In[21]:


#Interpolación de la anomalía
f_interp = InterpolatedUnivariateSpline(x, bou, k=3)
x_2 = linspace(0, 6000)
y_2 = f_interp(x_2)

plt.plot(x_2, y_2, label='Interpolación de datos')
plt.plot(x, bou, 'x', mew=3, label='Datos medidos')
plt.title("Anomalía de Bouguer")
plt.legend()


# In[26]:


mitad2 = max(y_2)/2 #Minimo medio de la anomalía interpolada
print (mitad2)

idx = np.argwhere(np.diff(np.sign(y_2 - mitad2))).flatten() #Obtiene el índice en x_domo del intercepto en la grafica con mitad2
half2 = x_2[idx] #El índice positivo es el halfwidth de la campana
print(half2)

