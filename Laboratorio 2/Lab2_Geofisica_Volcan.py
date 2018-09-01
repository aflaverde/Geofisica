
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
import numpy as np
import math
from scipy.interpolate import InterpolatedUnivariateSpline

G=6.67e-11
pi=np.pi
roS=2700


# In[2]:


x = [0, 623, 1246, 1869,2492, 3115, 3738, 4361, 4984, 5607, 6230, 6853]
bou  = [0.180, 0.373, 2.425, 4.960, 8.703, 12.615, 14.388, 15.065, 13.087, 10.927, 9.249, 7.131]


# In[7]:


f_interp = InterpolatedUnivariateSpline(x, bou, k=3) #Funcion interpolada
x_2 = linspace(0, 7000)
y_interp = f_interp(x_2)
plt.plot(x_2, y_interp, label='Interpolación de datos')
plt.plot(x, bou, 'x', mew=3, label='Datos medidos')
plt.title("Anomalía de Bouger")
plt.legend()

mitad2 = max(y_interp)/2 #Minimo medio de la anomalía interpolada

idxinter = np.argwhere(np.diff(np.sign(y_interp - mitad2))).flatten() #Obtiene el índice en x_domo del intercepto en la grafica con mitad2
half2 = x_2[idxinter] #El índice positivo es el halfwidth de la campana
print(half2)

dist_med2 = (half2[1]-half2[0])/2
print(dist_med2)

prof_real = dist_med2 * 1.306 #Arroja la profundidad de la formacion debajo del volcan
prof_real

