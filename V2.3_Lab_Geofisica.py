
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
import numpy as np
import math

####Punto A

G=6.67e-11
pi=np.pi
roS=2700


x=linspace(-500,500,1001) #crea un arreglo


def funcionG(r,z, roE):
    g=(4/3)*pi*G*(r**3)*(roE-roS)*(z/((x**2+z**2)**(3/2)))
    return g


# In[2]:


####Punto B
##Dens. variable

#graf 1
z1=200
r=50
y1=funcionG(r,z1, 2750)
plt.plot(x,y1)

#graf 2
z2=200
y2=funcionG(r,z2, 2800)
plt.plot(x,y2)

#graf 3
z3=200
y3=funcionG(r,z3, 2600)
plt.plot(x,y3)

##Prof. variable

#graf 4
z4=100
y4=funcionG(r,z4, 2800)
plt.plot(x,y4)

#graf 5
z5=250
y5=funcionG(r,z5, 2800)
plt.plot(x,y5)

#graf 6
z6=400
y6=funcionG(r,z6, 2800)
plt.plot(x,y6)
plt.title("g vs x")
plt.xlabel("x (m)")
plt.ylabel("g (m/s^2)")


# In[3]:


####Punto C
##Dens. variable

mitad1 = max(y1)/2 #Max g1 medio

mitad2 = max(y2)/2 #Max g2 medio

mitad3 = min(y3)/2 #Max g3 medio

idx1 = np.argwhere(np.diff(np.sign(y1 - mitad1))).flatten() #Obtiene el índice en x del intercepto de cada gráfica con max/2
half1=x[idx1] #El índice positivo es el halfwidth de cada campana
print(half1)

idx2 = np.argwhere(np.diff(np.sign(y2 - mitad2))).flatten() 
half2 = x[idx2]
print(half2)

idx3 = np.argwhere(np.diff(np.sign(y3 - mitad3))).flatten() 
half3 = x[idx3]
print(half3)

##Prof. variable

mitad4 = max(y4)/2 #Max g1 medio

mitad5 = max(y5)/2 #Max g2 medio

mitad6 = max(y6)/2 #Max g3 medio

idx4 = np.argwhere(np.diff(np.sign(y4 - mitad4))).flatten() #Obtiene el índice en x del intercepto de cada gráfica con max/2
half4=x[idx4] #El índice positivo es el halfwidth de cada campana
print(half4)

idx5 = np.argwhere(np.diff(np.sign(y5 - mitad5))).flatten() 
half5 = x[idx5]
print(half5)

idx6 = np.argwhere(np.diff(np.sign(y6 - mitad6))).flatten() 
half6 = x[idx6]
print(half6)


# In[4]:


coef1 = z1/half1[1]  ##Coeficientes de z / x(1/2)
print(coef1)

coef2 = z2/half2[1]
print(coef2)

coef3 = z3/half3[1]
print(coef3)

coef4 = z4/half4[1]
print(coef4)

coef5 = z5/half5[1]
print(coef5)

coef6 = z6/half6[1]
print(coef6)


# In[5]:


####Punto D
x_domo = [0, 700, 1360, 1940, 2420, 2840, 3500, 4080, 5060, 5840]
g_domo = [-1.84e-6, -3.42e-6, -6.67e-6, -1.23e-5, -1.92e-5, -2.39e-5, -2.04e-5, -1.2e-5, -4.33e-6, -2.12e-6]
x_array = np.array(x_domo)
g_array = np.array(g_domo)

plt.plot(x_array, g_array, label='')
plt.title("Anomalía gravitacional de un domo de sal")
plt.ylabel("g (m/s^2)")
plt.xlabel("x (m)")

mitad_domo = min(g_array)/2 #Minimo medio de la anomalía

idx_domo = np.argwhere(np.diff(np.sign(g_array - mitad_domo))).flatten() #Obtiene el índice en x_domo del intercepto en la grafica con mitad_diap
half_domo = x_array[idx_domo] #El índice positivo es el halfwidth de la campana
print(half_domo)

dist_med = (half_domo[1]-half_domo[0])/2
print(dist_med)

prof_domo = dist_med * coef1
prof_domo


# In[6]:


##PARTE 2

pS=2700

def funcion_losa(h,z0,pP):  #h: grosor, z0: prof, pP: densidad losa
    g2=2*G*h*(pP-pS)*((pi/2)+np.arctan(x/z0))
    return g2

##Grosor variable

anom_1=funcion_losa(50, 30, 3000)
plt.plot(x, anom_1, label='h=50')

anom_2=funcion_losa(100, 30, 3000)
plt.plot(x, anom_2, label='h=100')

anom_3=funcion_losa(200, 30, 3000)
plt.plot(x, anom_3, label='h=200')
plt.title("Anomalía gravitacional de una losa horizontal (Grosor variable)")
plt.legend()
plt.ylabel("g (m/s^2)")
plt.xlabel("x (m)")


# In[7]:


##Profundidad variable

anom_4=funcion_losa(50, 30, 3000)
plt.plot(x, anom_4, label='z=30')

anom_5=funcion_losa(50, 60, 3000)
plt.plot(x, anom_5, label='z=60')

anom_6=funcion_losa(50, 100, 3000)
plt.plot(x, anom_6, label='z=100')
plt.title("Anomalía gravitacional de una losa horizontal (Profundidad variable)")
plt.legend()
plt.ylabel("g (m/s^2)")
plt.xlabel("x (m)")


# In[8]:


##Densidad variable

anom_7=funcion_losa(50, 30, 2600)
plt.plot(x, anom_7, label='p_e=2600')

anom_8=funcion_losa(50, 30, 2750)
plt.plot(x, anom_8, label='p_e=2750')

anom_9=funcion_losa(50, 30, 3000)
plt.plot(x, anom_9, label='p_e=3000')
plt.title("Anomalía gravitacional de una losa horizontal (Densidad variable)")
plt.legend()
plt.ylabel("g (m/s^2)")
plt.xlabel("x (m)")


# In[12]:


# Derivada
##h variable
der_1 = np.diff(anom_1)/np.diff(x) #Definicion numpy de derivada

der_2 = np.diff(anom_2)/np.diff(x)
plt.plot(x[1:], der_2, label='p_e=3000')

der_3 = np.diff(anom_3)/np.diff(x)

##z variable
der_4 = np.diff(anom_4)/np.diff(x)
plt.plot(x[1:], der_4, label='p_e=3000')

der_5 = np.diff(anom_5)/np.diff(x)

der_6 = np.diff(anom_6)/np.diff(x)

##p variable
der_7 = np.diff(anom_7)/np.diff(x)
plt.plot(x[1:], der_7, 'b', label='p_e=2600')

der_8 = np.diff(anom_8)/np.diff(x)
plt.plot(x[1:], der_8, label='p_e=2750')

der_9 = np.diff(anom_9)/np.diff(x)

plt.title("Primera derivada")
plt.legend()
plt.ylabel("g (m/s^2)")
plt.xlabel("x (m)")


# In[11]:


##h variable
fprime1 = (der_1[1:] - der_1[:(len(der_1)-1)])/(x[1]-x[0]) #Definición formal de derivada (límite)

fprime2 = (der_2[1:] - der_2[:(len(der_2)-1)])/(x[1]-x[0])
plt.plot(x[2:], fprime2, label='p_e=3000')

fprime3 = (der_3[1:] - der_3[:(len(der_3)-1)])/(x[1]-x[0])

##z variable
fprime4 = (der_4[1:] - der_4[:(len(der_4)-1)])/(x[1]-x[0])
plt.plot(x[2:], fprime4, label='p_e=3000')

fprime5 = (der_5[1:] - der_5[:(len(der_5)-1)])/(x[1]-x[0])

fprime6 = (der_6[1:] - der_6[:(len(der_6)-1)])/(x[1]-x[0])

##p variable
fprime7 = (der_7[1:] - der_7[:(len(der_7)-1)])/(x[1]-x[0])
plt.plot(x[2:], fprime7, 'b', label='p_e=2600')

fprime8 = (der_8[1:] - der_8[:(len(der_8)-1)])/(x[1]-x[0])
plt.plot(x[2:], fprime8, label='p_e=2750')

fprime9 = (der_9[1:] - der_9[:(len(der_9)-1)])/(x[1]-x[0])

plt.title("Segunda derivada")
plt.legend()
plt.ylabel("g (m/s^2)")
plt.xlabel("x (m)")

